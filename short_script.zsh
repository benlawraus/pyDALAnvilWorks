  mkdir work1
  cd work1 || exit
  python3 -m venv ./venv
  source venv/bin/activate
  pip3 install pydal
  pip3 install pytest
  pip3 install pytest-tornasync
  pip3 install strictyaml
  git clone https://github.com/benlawraus/pyDALAnvilWorks.git
  git clone https://github.com/anvilistas/anvil-extras.git
  mv anvil-extras anvil_extras
  rm -rf ./anvil_extras/tests
  python3 -m pytest
