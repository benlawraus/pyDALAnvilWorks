anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
app_on_laptop=theDirectory/OfYour/pyDALAnvilWorks
cd $anvil_app || exit 1
if git pull origin master; then
    echo "git pull completed with no errors."
else
    echo "git pull errors initiated premature exit."
    exit 1
fi
rsync -rv --exclude='_anvil_designer.py' --exclude='__pycache__/' --include='*.py' --exclude='*.*' $app_on_laptop/client_code/ $anvil_app/client_code
rsync -rv $app_on_laptop/server_code/ $anvil_app/server_code
if git commit -am "Edited on laptop"; then
    echo "git commit completed with no errors."
else
    echo "git commit errors initiated premature exit.
    Was trying to commit files at ${anvil_app}."
    exit 1
fi
if git push origin master; then
    echo "git push completed with no errors."
else
    echo "git push errors initiated premature exit.
    Was trying to push to anvil.works."
    exit 1
fi
cd $app_on_laptop || exit 1
if git commit -am "Before updating yaml from anvil.works"; then
    echo "git commit completed with no errors."
else
    echo "git commit errors initiated premature exit."
    exit 1
fi
rsync -rv --include='*.yaml' --exclude='__pycache__/' --exclude='*.*' $anvil_app/client_code/ $app_on_laptop/client_code
echo "Regenerating _anvil_designer.py files in ${PWD}"
python3 -m _anvil_designer.generate_files