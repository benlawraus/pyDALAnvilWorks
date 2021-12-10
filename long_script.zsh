mkdir work
cd work || exit
setopt interactivecomments
# allow comments for zsh
# create a virtualenv
python3 -m venv ./venv
source venv/bin/activate
# these are used by yaml2schema
pip3 install datamodel-code-generator
pip3 install strictyaml
# clone anvil demo app
myAnvilApp="pyDALAnvilWorksApp"
myAnvilGit="ssh://youranvilworksusername@anvil.works:2222/yourprojectcode.git"
git clone $myAnvilGit $myAnvilApp
# clone yaml2schema
git clone https://github.com/benlawraus/yaml2schema.git
# clone the anvil adapter
git clone https://github.com/benlawraus/pyDALAnvilWorks.git
# rename it to something else so we can use it to work there
my_work_dir="mywork"
mv pyDALAnvilWorks $my_work_dir
###################################################
# create the pydal definitions file in our work directory so we can save our tests on github
mkdir $my_work_dir/yaml2schema
mkdir $my_work_dir/yaml2schema/input
mkdir $my_work_dir/yaml2schema/output
cp  $myAnvilApp/anvil.yaml $my_work_dir/yaml2schema/input
# anvil yaml too broad for what we need, so refine it with anvil_refined.yaml.
# For your project, you may want to also refine the anvil.yaml schema
cp yaml2schema/src/yaml2schema/input/anvil_refined.yaml $my_work_dir/yaml2schema/input
# finally! create the database schema
cd $my_work_dir/yaml2schema || exit
python3 ../../yaml2schema/src/yaml2schema/main.py
# take it and use it in our test directory
cd ..
mv yaml2schema/output/pydal_def.py tests
# copy our server and client files
cp ../$myAnvilApp/server_code/*.py server_code
cp ../$myAnvilApp/client_code/*.py client_code
# install anvil_extras (optional, only if you use that awesome project)
git clone https://github.com/anvilistas/anvil-extras.git
# why the hyphen when we need the underscore ?!?
mv anvil-extras anvil_extras
# but we don't want to run anvil_extras tests...
rm -rf ./anvil_extras/tests
# install the giant dependencies
pip3 install pyDAL
pip3 install pytest
pip3 install pytest-tornasync
python3 -m pytest
