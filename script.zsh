mkdir "work"
cd work
setopt interactivecomments  # allow comments for zsh
# create a virtualenv
python3 -m venv ./venv
source venv/bin/activate
# these are used by yaml2schema
pip3 install datamodel-code-generator
pip3 install strictyaml
# clone anvil demo app
myAnvilApp="pyDALAnvilWorksApp"
myAnvilGit="ssh://ben.lawrence%40east-elec.com@anvil.works:2222/NX66PIIAF3ECPA55.git"
git clone $myAnvilGit $myAnvilApp
# clone yaml2schema
git clone https://github.com/benlawraus/yaml2schema.git
# clone the anvil adapter
git clone https://github.com/benlawraus/pyDALAnvilWorks.git
# rename it to something else so we can use it to work there
myworkdir="mywork"
mv pyDALAnvilWorks $myworkdir
###################################################
# create the pydal definitions file in our work directory so we can save our tests on github
mkdir $myworkdir/temp
mkdir $myworkdir/temp/input
mkdir $myworkdir/temp/output
cp  $myAnvilApp/anvil.yaml $myworkdir/temp/input
# anvil yaml too broad for what we need, so refine it with anvil_refined.yaml.
# For your project, you may want to also refine the anvil.yaml schema
cp yaml2schema/src/yaml2schema/input/anvil_refined.yaml $myworkdir/temp/input
# finally! create the database schema
cd $myworkdir/temp
python3 ../../yaml2schema/src/yaml2schema/main.py
# take it and use it in our test directory
cd ..
mv temp/output/pydal_def.py tests
# copy our server and client files
cp ../$myAnvilApp/server_code/*.py server_code
cp ../$myAnvilApp/client_code/*.py client_code
pip3 install pytest
python3 -m pytest
