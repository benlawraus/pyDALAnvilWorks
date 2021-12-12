What is it?
------------
To allow you to:
    * Use any database while testing your `anvil.works <https://anvil.works>`_ app.
    * Create and run tests using pytest. These tests would be for the python in client_side forms, as well as server_side python. No testing of javascript UI can be done here.
    * Most importantly: use **PyCharm** more with auto-complete on forms.

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
`tests` directory.

Also create a `database` directory there to put all your database files. And! a `template` directory
containing the class definitions of the client form components. The class definitions are written during the first run
(see ``_anvil_designer``).

A csv file can be exported from your anvil.works database and imported into your sqlite using  `pyDal <http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#Exporting-and-importing-data>`_,
but really, you should generate dummy data during your tests anyway.

Your directory structure on your laptop will then look like this:

    - anvil  (from this repo)
    - _anvil_designer (from this repo)
    - client_code  (git-cloned from anvil.works)
    - server_code  (git-cloned from anvil.works)
    - tests (your tests you run on your laptop)
        - database  (your sqlite and pydal files to run your database on your laptop)
        - pydal_def.py  # generated from anvil.yaml using yaml2schema
        - test1.py
    - anvil.yaml (git-cloned from anvil.works)


It should be mentioned that the top directory containing all of the above should be marked as the **sources root**.

Also depending on your project structure, you might need to do something like::

    try:
        # when running on anvil.works
        OWN_COMPUTER = False
        from portable_classes import Phone, Email, Contact
    except ImportError:
        # when running on your laptop
        from server_code.DEBUG import OWN_COMPUTER
        from client_code.portable_classes import Phone, Email, Contact

Yes, this is annoying. Maybe there is a better way...

For client code tests, if there is no ``_anvil_designer.py`` in the form directory, it will be generated after the first run.
So, similarly in your *Form* code, (after first run, you will see a ``._anvil_designer.py``)::

    try:
        from ._anvil_designer import ContactFormTemplate
    except ImportError:
        from _anvil_designer import ContactFormTemplate

    import anvil.server
    import anvil.users

    class ContactForm(ContactFormTemplate):
        etc

``_anvil_designer`` allows testing on code on the client side. (See ``test_ContactForm.py`` for some pytests) and auto-complete on form components.


Push Pull Scripts
------------------
In your average day, you will edit code and push and pull your changes to *anvil.works*.
Two scripts are included here to make that easier : ``git_pull_from_anvil_works.zsh`` and ``git_push_to_anvil_works.zsh``.
They assume you have your anvil app already git-cloned on your laptop.

Anvil-Extras
--------------
`Anvil-Extras <https://github.com/anvilistas/anvil-extras>`_ is really nice, especially its publish-subscribe module and its
navigation module. So as to use it, there is an ``anvil_extras`` folder here too, but none of its tests or its functionality
have been tested with pyDALAnvilWorks repo.


This project is in its infancy...

Examples
---------

Simple
^^^^^^
This repo has a copy of an anvil.works app already there. So, you can download this repo and run these few commands in your terminal.
The files in the form directories ``_anvil_designer.py`` are generated on the first run, so delete those files if you update your forms UI::

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


Complicated
^^^^^^^^^^^
But if you want to see how to use your own anvil.works app here, try to understand this script.

It will run in your terminal (good for python 3.7+). Before doing, make sure you
create a copy of the example app in your `anvil.works` account.

`CLONE ME <https://anvil.works/build#clone:XWM5WQ66ONSRYYXL=WJUZGODLYP2JSYWR3XU2Y2XD>`_

You need to then substitute your clone example for `myAnvilGit` in the following script::

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


See real tests in the `tests` directory.

Done
----
The following will run on your laptop (without internet) with a sqlite database::

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

In your client tests::

    c_form = ContactForm(contact=contact)
    assert x == c_form.text_box_name.text
    assert x == c_form.repeating_panel_1.items[0]['text']

Gotchas
-------
Updating Rows
^^^^^^^^^^^^^^
*anvil.works* allows you update your database using::

    row['name']="Rex Eagle"

This is allowed in this wrapper, with the allowance that no sqlite row will be update, only the object ``row`` will be
updated. To update the database row, you have to use ``row.update()``

Package and Module Forms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the anvil.works, there are package forms and module forms. pyDALAnvilWorks was built to handle package forms.


to be continued....

Thank You
-----------
This work is sponsored by `East Electronics <https://east-elec.com>`_.

