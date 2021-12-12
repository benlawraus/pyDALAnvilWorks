anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
pyDALAnvilWorks=theDirectory/OfYour/pyDALAnvilWorks
cd $anvil_app || exit
git pull origin master
rsync -r $anvil_app/client_code/ $pyDALAnvilWorks/client_code
rsync -r $anvil_app/server_code/ $pyDALAnvilWorks/server_code
rsync $anvil_app/anvil.yaml $pyDALAnvilWorks
rm -f $pyDALAnvilWorks/client_code/*/_anvil_designer.py
cd $pyDALAnvilWorks || exit
python -m _anvil_designer.generate_files
