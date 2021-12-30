echo "~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~  -  ~"
anvil_app="theDirectory/OfYour/ClonedAnvilWorksApp"
app_on_laptop="theDirectory/OfYour/pyDALAnvilWorks"
yaml2schema="theDirectory/ofYour/yaml2schema"
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
  echo "${anvil_app}  not there. git clone your app from anvil.works."
  exit 1
fi
# copy anvil.yaml and anvil_refined.yaml (anvil_refined.yaml lives with your app_on_laptop)
anvil_yaml=$anvil_app/anvil.yaml
anvil_refined_yaml=$app_on_laptop/anvil_refined.yaml
echo "Using ${anvil_yaml} and ${anvil_refined_yaml} to generate pydal_def.py"
cp "$anvil_app"/anvil.yaml "$yaml2schema"/src/yaml2schema/input/
if ! cp "$app_on_laptop"/anvil_refined.yaml "$yaml2schema"/src/yaml2schema/input/; then
    echo "No anvil_refined.yaml. Continuing..."
fi
cd "$yaml2schema"/src/yaml2schema || exit 1

# check that everything went ok
if python3 main.py; then
    echo "yaml2schema completed with no errors."
else
    echo "pydal_def not generated. yaml2schema interrupted."
    exit 1
fi
# save before copying
cd "$app_on_laptop" || exit 1
if git commit -am "Before generating new pydal_def.py"; then
    echo "git commit completed with no errors."
else
    echo "pydal_def not copied. git commit errors."
    exit 1
fi
# copy the pyDAL definition file to app
cp "$yaml2schema"/src/yaml2schema/output/pydal_def.py "$app_on_laptop"/tests/
echo "Erasing current database."
rm -f "$app_on_laptop"/tests/database/*.table
rm -f "$app_on_laptop"/tests/database/*.log
rm -f "$app_on_laptop"/tests/database/*.sqlite
echo "Generating new database."
if python3 tests/pydal_def.py; then
    echo "New database generated with no errors."
else
    echo "pydal_def not copied. git commit errors."
    exit 1
fi
# Generate AppTables
if ! python3 -m _anvil_designer.generate_apptable; then
  echo "Crashed while generating AppTable.py."
    exit 1
fi

exit 0