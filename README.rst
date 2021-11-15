What is it?
------------
To allow you to use any database while testing your `anvil.works <https://anvil.works>`_ app.

How is it done?
---------------
The program uses `pyDAL <https://py4web.com/_documentation/static/en/chapter-07.html>`_ to substitute
the database interactions. This means you can git clone your app on your laptop and run some tests on it without
modifying your app or using the external server's database.

How to use it?
---------------
First, create your virtual environment and install pyDAL.

Copy this repo's directory structure into your cloned anvil.works app. Instead of calling the anvil.works routines, it will use
the local version instead.

Of course, you will need a complete mirror of your anvil.works external database. To set that up,
use this `converter <https://github.com/benlawraus/yaml2schema>`_. In your cloned anvil.works
app, there is a file called `anvil.yaml`. This file contains a description of your
database schema. The `converter <https://github.com/benlawraus/yaml2schema>`_ will read
the `anvil.yaml` and generate a `pyDAL <https://py4web.com/_documentation/static/en/chapter-07.html>`_
definition file (`pydal_def.py`) that you can use to run your tests. Place `pydal_def.py` into your
`tests` directory. Also create a `database` directory there to put all your database files.

A csv file can be exported from your anvil.works database and imported into your sqlite using  `pyDAL`.
But really, you should generate dummy data during your tests anyway.

Your directory structure on your laptop will then look like this::

    - anvil  (from this repo)
    - client_code  (git-cloned from anvil.works)
    - server_code  (git-cloned from anvil.works)
    - tests (your tests you run on your laptop)
        - database  (your sqlite and pydal files to run your database on your laptop)
        - pydal_def.py  # generated from anvil.yaml using yaml2schema
        - test1.py
    - anvil.yaml (git-cloned from anvil.works)

Examples
---------
This will run in your terminal (good for python 3.7+). Before doing, make sure you
create a copy of the example app in your `anvil.works` account. The link is
`clone example <https://anvil.works/build#clone:NX66PIIAF3ECPA55=JEYUW7CMGRTSBFXCKYRVXSI4>`_::

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
    myAnvilGit="ssh://xxxxxxxxxxxxxxxxxxx@anvil.works:2222/xxxxxxxxxxxxxxxx.git"
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
    pip3 install pyDAL
    pip3 install pytest
    pip3 install pytest-tornasync
    python3 -m pytest


See real tests in the `tests` directory.

Done
----
The following will run on your laptop (without internet) with a database table `contact`::

    user = anvil.users.get_user()
    user = anvil.users.get_by_id(user_ref)
    contact_row = app_tables.contact.get_by_id(contact_ref)
    contact_id = contact_row.get_id()
    contact_row = app_tables.contact.add_row(**contact_dict)
    contact_row.delete()
    contact_row.update(name="Rex Eagle", age=6)
    contact_row = app_tables.contact.get(name="Rex Eagle", age=6)
    rows = app_tables.contact.search(created_on=some_datetime)
    rows = app_tables.contact.search(tables.order_by('name', ascending=False), created_on=created_on)
    rows = app_tables.contact.search(age=q.greater_than(33))
    rows = app_tables.contact.search(age=q.greater_than_or_equal_to(33))
    rows = app_tables.contact.search(age=q.less_than(33))
    rows = app_tables.contact.search(age=q.less_than_or_equal_to(33))
    rows = app_tables.contact.search(age=q.less_than_or_equal_to(33))
    rows = app_tables.contact.search(age=q.not_(33))
    rows = app_tables.contact.search(q.all_of(q.any_of(age=45, name="Kevin"), created_by=user))
    app_tables.contact.list_columns()
    dict(row)  # will produce extra pyDAL attributes so needs filtering
    @anvil.server.callable
    @anvil.server.callable(require_user=True) # or some_function)
    @anvil.server.call("server_function")

to be continued....

