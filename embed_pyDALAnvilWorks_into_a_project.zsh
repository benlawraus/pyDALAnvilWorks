# myAnvilGit="ssh://youranvilworksusername@anvil.works:2222/gobblygook.git"
myAnvilGit="ssh://ben.lawrence%40east-elec.com@anvil.works:2222/XWM5WQ66ONSRYYXL.git"

echo "What this script does:"
echo "Clones the anvil app from anvil.works"
echo "Copies it to a work directory."
echo "Git submodule yaml2schema in order to retrieve database information from anvil.yaml"
echo "Git submodule pyDALAnvilWorks in order to insert anvil.works wrappers."
echo "In work directory, create a virtualenv and pip install dependencies."
mkdir my_work
cd my_work || exit 1
my_work=$(pwd)
echo "my_work is $my_work"
# what your anvil app is called
app_on_laptop="$my_work/pyDALAnvilWorksDev"
anvil_app="$app_on_laptop/pyDALAnvilWorksApp"
yaml2schema="$app_on_laptop/yaml2schema"
pyDALAnvilWorks="$app_on_laptop/pyDALAnvilWorks"
# setopt interactivecomments
# allow comments for zsh
# Create new rep
mkdir "$app_on_laptop"
cd "$app_on_laptop" || exit 1
git init
git remote add origin https://github.com/benlawraus/pyDALAnvilWorksDev.git
git pull origin master
# Add anvil.works app as a submodule
echo "git submodule to ${anvil_app} .."
if ! git submodule add "$myAnvilGit" "$anvil_app"; then
    echo "Errors occurred. Exiting."
    exit 1
fi
# add yaml2schema as a submodule
echo "git submodule to ${yaml2schema} .."
if ! git submodule add https://github.com/benlawraus/yaml2schema.git "$yaml2schema"; then
    echo "Errors occurred. Exiting."
    exit 1
fi
# add pyDALAnvilWorks as a submodule
echo "git submodule to ${pyDALAnvilWorks} .."
if ! git submodule add https://github.com/benlawraus/pyDALAnvilWorks.git "$pyDALAnvilWorks"; then
    echo "Errors occurred. Exiting."
    exit 1
fi
rm -rf "$app_on_laptop"/anvil_extras  # just in case there is one there...

cd "$app_on_laptop" || exit 1
# create a virtualenv
echo "Create virtualenv .."
if ! python3 -m venv ./venv; then
    exit 1
fi
echo "Activate virtualenv ${VIRTUAL_ENV} .."
source venv/bin/activate
if ! [[ $VIRTUAL_ENV = *"${app_on_laptop}"* ]]; then
    echo "Errors occurred. Exiting."
    exit 1
fi

# these are used by yaml2schema
# pip3 install datamodel-code-generator # lets not generate class models, do not need them.
if ! pip3 install strictyaml; then
  echo "pip3 errors while installing strictyaml"
  exit 1
fi
# install these giant dependencies
pip3 install pyDAL
pip3 install pytest
pip3 install pytest-tornasync

####################### OPTIONAL ##########################
# install anvil_extras (optional, only if you use that sweet project)
cd "$app_on_laptop" || exit 1
git clone https://github.com/anvilistas/anvil-extras.git
# why the hyphen when we need the underscore ?!?
mv anvil-extras anvil_extras
# but we don't want to run anvil_extras tests...
rm -rf ./anvil_extras/tests
############################################################
# generate pydal_def.py
echo "Generate pydal_def.py in the test directory .."
chmod +x "$pyDALAnvilWorks"/yaml2schema.zsh || exit 1
if ! "$pyDALAnvilWorks"/yaml2schema.zsh "$anvil_app" "$app_on_laptop" "$yaml2schema"; then
    echo "Errors occurred. Exiting."
    exit 1
fi
# copy our server and client files
echo "Copy server and client files .."
chmod +x "$app_on_laptop"/git_pull_from_anvil_works.zsh || exit 1
if ! ./git_pull_from_anvil_works.zsh "$anvil_app" "$app_on_laptop"; then
    echo "Errors occurred. Exiting."
    exit 1
fi
cd "$app_on_laptop" || exit 1
