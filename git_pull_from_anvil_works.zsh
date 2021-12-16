anvil_app="theDirectory/OfYour/GitCloned/AnvilApp"
app_on_laptop="theDirectory/OfYour/pyDALAnvilWorks"
if [ $# -eq 2 ]
  then
    anvil_app=$1
    app_on_laptop=$2
else
    echo "No arguments supplied. Using:
     ${anvil_app}
     ${app_on_laptop}"
fi

cd "$app_on_laptop" || exit 1
git commit -am "Before a pull from anvil.works"
cd "$anvil_app" || exit 1
if git pull origin master; then
    echo "git pull completed with no errors."
else
    echo "git pull errors initiated premature exit."
    exit 1
fi
if ! rsync -r "$anvil_app"/client_code/ "$app_on_laptop"/client_code; then
    exit 1
fi
rsync -r "$anvil_app"/server_code/ "$app_on_laptop"/server_code
rsync "$anvil_app"/anvil.yaml "$app_on_laptop"
cd "$app_on_laptop" || exit 1
echo "Regenerating _anvil_designer.py files in ${PWD}"
python -m _anvil_designer.generate_files
