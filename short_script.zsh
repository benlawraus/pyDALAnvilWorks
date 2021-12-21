mkdir work1
cd work1 || exit 1
python3 -m venv ./venv
source venv/bin/activate
if ! [[ $VIRTUAL_ENV = *"${app_on_laptop}"* ]]; then
  echo "Could not activate virtualenv."
  exit 1
fi
echo "Activating virtualenv ${VIRTUAL_ENV}."
if ! pip3 install strictyaml; then
  echo "pip3 errors while installing strictyaml"
  exit 1
fi
pip3 install pydal
pip3 install pytest
pip3 install pytest-tornasync
git clone https://github.com/benlawraus/pyDALAnvilWorks.git
cd pyDALAnvilWorks || exit 1
git clone https://github.com/anvilistas/anvil-extras.git
mv anvil-extras anvil_extras
rm -rf ./anvil_extras/tests
if ! python3 -m _anvil_designer.generate_files; then
  echo "Crashed while regenerating the _anvil_designer.py files."
    exit 1
fi
python3 -m pytest
