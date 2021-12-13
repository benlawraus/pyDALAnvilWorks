anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
app_on_laptop=theDirectory/OfYour/pyDALAnvilWorks
cd $anvil_app || exit
git pull origin master
rsync -rv --exclude='_anvil_designer.py' --exclude='__pycache__' --include='*.py' --exclude='*.*' $app_on_laptop/client_code/ $anvil_app/client_code
rsync -rv $app_on_laptop/server_code/ $anvil_app/server_code
git commit -am "Edited on laptop"
git push origin master
cd $app_on_laptop || exit
git commit -am "Before updating yaml from anvil.works"
rsync -rv --include='*.yaml' --exclude='__pycache__' --exclude='*.*' $anvil_app/client_code/ $app_on_laptop/client_code
python3 -m _anvil_designer.generate_files