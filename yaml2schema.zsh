echo "~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~"
anvil_app="theDirectory/OfYour/ClonedAnvilWorksApp"
app_on_laptop="theDirectory/OfYour/pyDALAnvilWorks"
yaml2schema="theDirectory/of/yaml2schema (downloaded from https://github.com/benlawraus/yaml2schema)"
if [ $# -eq 3 ]
  then
    anvil_app=$1
    app_on_laptop=$2
    yaml2schema=$3
else
    echo "No arguments supplied. Using:
     ${anvil_app}
     ${app_on_laptop}
     ${yaml2schema}"
fi
echo "Copies anvil.yaml from ${anvil_app} and generates a new pydal_def.py in ${app_on_laptop}"
echo "Also, updates AppTables.py to reflect correct table names with their column names and types."
# check that directories exists, exit otherwise
if [ ! -d "$yaml2schema" ]; then
  echo "${yaml2schema} not there. Use https://github.com/benlawraus/yaml2schema"
  exit 1
fi
if [ ! -d "$app_on_laptop" ]; then
  echo "${app_on_laptop} not there.
This is your development space and should contain all the tools such pyDALAnvilWorks."
  exit 1
fi
if [ ! -d "$anvil_app" ]; then
  echo "${anvil_app}  not there. git your app from anvil.works."
  exit 1
fi
# copy anvil.yaml and anvil_refined.yaml (anvil_refined.yaml lives with your app_on_laptop)
anvil_refined_yaml=$app_on_laptop/anvil_refined.yaml
echo "Using anvil.yaml and ${anvil_refined_yaml} to generate pydal_def.py"
cp "$anvil_app"/anvil.yaml "$yaml2schema"/src/yaml2schema/input/ || exit 1
if ! cp "$app_on_laptop"/anvil_refined.yaml "$yaml2schema"/src/yaml2schema/input/; then
  echo "No anvil_refined.yaml. Continuing..."
fi
cd "$yaml2schema"/src/yaml2schema || exit 1
if ! [[ $VIRTUAL_ENV = *"${app_on_laptop}"* ]]; then
  echo "No virtual env is activated."
  exit 1
fi

# check that everything went ok
echo "Use yaml2schema .."
if ! python3 main.py; then
    echo "pydal_def not generated. yaml2schema interrupted."
    exit 1
fi
# copy the pyDAL definition file to app
if ! cp "$yaml2schema"/src/yaml2schema/output/pydal_def.py "$app_on_laptop"/tests/; then
  echo "Create tests directory .."
  mkdir "$app_on_laptop"/tests || exit 1
  mkdir "$app_on_laptop"/tests/database || exit 1
  cp "$yaml2schema"/src/yaml2schema/output/pydal_def.py "$app_on_laptop"/tests/ || exit 1
fi
echo "Erasing current database."
rm -f "$app_on_laptop"/tests/database/*.table
rm -f "$app_on_laptop"/tests/database/*.log
rm -f "$app_on_laptop"/tests/database/*.sqlite
echo "Generating new pydal database schema (pydal_def.py)."
# check that directories are there and writable
if ! python3 tests/pydal_def.py; then
    echo "Error when generating database files. Exiting."
    exit 1
fi
# Generate AppTables
if ! python3 -m _anvil_designer.generate_apptable; then
  echo "Crashed while generating AppTable.py."
    exit 1
fi

exit 0
