myAnvilGit="ssh://youranvilworksusername@anvil.works:2222/gobblygook.git"

mkdir my_work
cd my_work || exit 1
my_work=$(pwd)
echo "my_work is $my_work"
# what your anvil app is called
anvil_app="$my_work/yourAnvilApp"

app_on_laptop="$my_work/myDevelopmentOnLaptop"
yaml2schema="$my_work/yaml2schema"
# setopt interactivecomments
# allow comments for zsh
# clone anvil demo app
if git clone "$myAnvilGit" "$anvil_app"; then
    echo "git clone to ${anvil_app} completed with no errors."
else
    echo "Errors for git clone  to ${anvil_app} initiated premature exit."
    exit 1
fi
# clone yaml2schema
git clone https://github.com/benlawraus/yaml2schema.git
# clone the anvil adapter
git clone https://github.com/benlawraus/pyDALAnvilWorks.git "$app_on_laptop"
rm -rf "$app_on_laptop"/anvil_extras  # just in case there is one there...

cd "$app_on_laptop" || exit 1
# create a virtualenv
if ! python3 -m venv ./venv; then
    exit 1
fi
source venv/bin/activate
if ! [[ $VIRTUAL_ENV = *"${app_on_laptop}"* ]]; then
  echo "Could not activate virtualenv."
  exit 1
fi
echo "Activating virtualenv ${VIRTUAL_ENV}."

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
cd "$app_on_laptop" || exit 1
chmod +x ./yaml2schema.zsh
if ! ./yaml2schema.zsh "$anvil_app" "$app_on_laptop" "$yaml2schema"; then
  exit 1
fi
# copy our server and client files
cd "$app_on_laptop" || exit 1
chmod +x git_pull_from_anvil_works.zsh
if ! ./git_pull_from_anvil_works.zsh "$anvil_app" "$app_on_laptop"; then
    exit 1
fi
cd "$app_on_laptop" || exit 1

# Generate all the _anvil_designer.py files for every form.
if ! python3 -m _anvil_designer.generate_files; then
  echo "Crashed while regenerating the _anvil_designer.py files."
    exit 1
fi
# Run PyTest
python3 -m pytest
