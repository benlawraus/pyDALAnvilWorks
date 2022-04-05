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

#cd "$app_on_laptop" || exit 1
#git commit -am "Before a pull from anvil.works"
cd "$anvil_app" || exit 1
echo "Git pull the anvil.works app.."
if ! git pull origin master; then
    echo "git pull errors initiated premature exit."
    exit 1
fi
echo "Copy anvil app code to project directories.."
if ! rsync -a --delete-after "$anvil_app"/client_code/ "$app_on_laptop"/client_code; then
    echo "An error while syncing the anvil.works app client code to the project."
    exit 1
fi
rsync -a -v --delete-after "$anvil_app"/server_code/ "$app_on_laptop"/server_code
cp "$anvil_app"/anvil.yaml "$app_on_laptop"
cd "$app_on_laptop" || exit 1
echo "Regenerating _anvil_designer.py files in ${PWD}"
python -m _anvil_designer.generate_files
