anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
app_on_laptop=theDirectory/OfYour/pyDALAnvilWorks
if [ $# -eq 2 ]
  then
    anvil_app=$1
    app_on_laptop=$2
else
    echo "No arguments supplied. Using:
     ${anvil_app}
     ${app_on_laptop}"
fi

cd "$anvil_app" || exit 1
if git pull origin master; then
    echo "git pull from anvil completed with no errors (doing this before pushing...)"
else
    echo "git pull errors initiated premature exit."
    exit 1
fi
# use  --out-format='%n' if you want to list the rsync files copied
rsync -a --exclude='_anvil_designer.py' --exclude='__pycache__' --include='*.py' --include='*/' --exclude='*'  "$app_on_laptop"/client_code/ "$anvil_app"/client_code
rsync -a --exclude='__pycache__' --include='*.py' --include='*/' --exclude='*'  "$app_on_laptop"/server_code/ "$anvil_app"/server_code
if git commit -am "Edited on laptop"; then
    echo "git commit completed with no errors."
else
  if git diff --exit-code; then
      echo "${anvil_app} has no changes. Nothing to commit."
  else
    git add -A  --quiet
    if git commit -am "Edited on laptop" --quiet; then
      echo "git commit completed with no errors after adding new files.."
    else
      echo "git commit errors initiated premature exit after git add for ${anvil_app}"
      exit 1
    fi
  fi
fi
if git push origin master --quiet; then
    echo "git push to anvil.works completed with no errors."
else
    echo "git push to anvil.works errors initiated premature exit.
    Was trying to push to anvil.works."
    exit 1
fi
cd "$app_on_laptop" || exit 1
rsync -a --include='*.yaml' --include='*/' --exclude='*' "$anvil_app"/client_code/ "$app_on_laptop"/client_code
echo "Regenerating _anvil_designer.py files in ${PWD}"
python3 -m _anvil_designer.generate_files