anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
app_on_laptop=theDirectory/OfYour/pyDALAnvilWorks
cd $app_on_laptop || exit
git commit -am "Before a pull from anvil.works"
cd $anvil_app || exit
git pull origin master
rsync -r $anvil_app/client_code/ $app_on_laptop/client_code
rsync -r $anvil_app/server_code/ $app_on_laptop/server_code
rsync $anvil_app/anvil.yaml $app_on_laptop
cd $app_on_laptop || exit
python -m _anvil_designer.generate_files
