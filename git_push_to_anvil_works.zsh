anvil_app=theDirectory/OfYour/GitCloned/AnvilApp
pyDALAnvilWorks=theDirectory/OfYour/pyDALAnvilWorks
rsync -r --exclude='*/_anvil_designer.py' $pyDALAnvilWorks/client_code/ $anvil_app/client_code
rsync -r $pyDALAnvilWorks/server_code/ $anvil_app/server_code
cd $anvil_app || exit
git commit -am "Edited on laptop"
git push origin master
cd $pyDALAnvilWorks || exit
