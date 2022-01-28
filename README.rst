Note
====
The best way to start is `pyDALAnvilWorksDev <https://github.com/benlawraus/pyDALAnvilWorksDev>`_.
Basically it is an empty project. Clone it, change the directory name and then cd into the
directory. From there run its script with the address of the anvil.works app.
The script will:

* Install the git submodules:

    * your anvil.works app (using $myAnvilGit script argument)
    * `yaml2Schema <https://github.com/benlawraus/yaml2schema>`_ (to setup database)
    * `pyDALAnvilWorks <https://github.com/benlawraus/pyDALAnvilWorks>`_ (for testing client and server code.)
    * (optional `anvil-extras <https://github.com/anvilistas/anvil-extras>`_)

* Set up a virtualenv. In the virtualenv it pip-installs:

    *   `pyDAL <https://github.com/web2py/pydal>`_  (the database abstraction layer)
    *   `strictyaml <https://github.com/crdoconnor/strictyaml>`_ (to parse yaml files)
    *   `pytest <https://github.com/pytest-dev/pytest>`_
    *   `pytest-tornasync <https://github.com/eukaryote/pytest-tornasync>`_ (Parallel pytest helper for pyDAL)

* Use yaml2schema to setup database.
* Copy the files from the anvil app to the project directories
* Generate the ``_anvil_designer.py`` files for IDE auto-completion.
* Create scripts for push and pull to anvil server.


pyDALAnvilWorks
===============

What is it?
------------

This project exists in order to use `PyCharm <https://www.jetbrains.com/pycharm/>`_ (and other IDEs?) on
`anvil.works <https://anvil.works>`_ apps. It allow you to:

    * Use any local database while testing your `anvil.works <https://anvil.works>`_ app.
    * Create and run tests using pytest. These tests would be for the python in client_side forms, as well as server_side python. No testing of javascript UI can be done here.
    * Most importantly: use `PyCharm <https://www.jetbrains.com/pycharm/>`_ with auto-complete.


Recent Changes
---------------

..  csv-table::
    :header: "Before","Now"

    "No event handling","Can test for a .raise_event()"
    "error for form dropped into container","If your UI has drag-n-dropped form component it will import ok"
    "git cloned dependencies","use `pyDALAnvilWorksDev <https://github.com/benlawraus/pyDALAnvilWorksDev>`_"
    "scanty users wrapper","Complete anvil.users with more rugged login system to prevent flaky (py)tests."
    "","added auto-complete for: **apptables.TABLE.**"



How is it done?
---------------
Server-side
^^^^^^^^^^^
The program uses `pyDAL <https://github.com/web2py/pydal>`_ to substitute
the database interactions. This means you can git clone your app on your laptop and run some tests on it without
modifying your app or using the external server's database. The anvil.works commands have been turned into wrappers for
`pyDAL <https://github.com/web2py/pydal>`_ commands to your sqlite database on your laptop.

**But how is the sqlite database set-up?**

`Yaml2Schema <https://github.com/benlawraus/yaml2schema>`_ uses the
file called `anvil.yaml`. This file contains a description of your
database schema. `Yaml2Schema  <https://github.com/benlawraus/yaml2schema>`_ will read
the `anvil.yaml` and generate a `pyDAL <https://github.com/web2py/pydal>`_
definition file (`pydal_def.py`) that should be placed into your
`tests` directory. During your set-up, this file is executed and generates the sqlite database. Note that
if you want to run any other kind of database (e.g. postgresql, mysql etc) instead of sqlite,
you can do this by changing the adapter in `pydal_def.py`.
Take a look at the pyDAL's `documentation <https://py4web.com/_documentation/static/en/chapter-07.html>`_ to know more.

Client-side
^^^^^^^^^^^
For the client-side, `_anvil_designer.py` files are generated to mimic the UI on `anvil.works <anvil.works>`_. When your
client_side code meets a component it uses a dummy class from that file instead.

`_anvil_designer.py` will be referencing other dummy classes and functions in `_anvil_designer/componentsUI/`. If you want to
flesh them out a bit, you can do that there. Otherwise, most likely functions will have a `def function(*args):pass` format.

`_anvil_designer/componentsUI/` is basically the `anvil API docs <https://anvil.works/docs/api>`_ turned into python code.
All the methods and functions in the api are in this directory.
If your IDE is not auto-completing for a method, it probably is because an entry needs to be made in `anvil/__init__.py`
to point to that method in `_anvil_designer/componentsUI`. PyCharm is smart enough to find it.

How to use it?
---------------
Your directory structure on your laptop will look like this:

    - anvil  (from this repo)
    - _anvil_designer (from this repo)
    - client_code  (git-cloned from anvil.works)
    - server_code  (git-cloned from anvil.works)
    - tests (your tests you run on your laptop)
        - database  (your sqlite and pydal files to run your database on your laptop)
        - pydal_def.py  # generated from anvil.yaml using yaml2schema
        - test1.py # your test file
    - anvil.yaml (git-cloned from anvil.works)

Kick the Tires
^^^^^^^^^^^^^^
Download the repo and open it in `PyCharm <https://www.jetbrains.com/pycharm/>`_. Open a form (`__init__.py` in a form directory)
and test out the auto-complete.

Try and Use It
^^^^^^^^^^^^^^

One way is to git clone `pyDALAnvilWorksDev <https://github.com/benlawraus/pyDALAnvilWorksDev>`_. After downloading,
rename it and run the script with your anvil app link.

Once this is set-up use the push and pull scripts generated, to sync to and from your anvil app.

If you want to, it is possible to download your anvil.works database into your laptop's sqlite database.
A csv file can be exported from your anvil.works database and imported into your sqlite using  `pyDal <http://www.web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#Exporting-and-importing-data>`_,
but really, you should generate dummy data during your tests anyway.

Laptop Testing an Anvil.Works app.
----------------------------------

server_code
^^^^^^^^^^^^
The `anvil.yaml` file is used to generate the database and the `AppTable` class. The `AppTable` class is needed
to have auto-complete in your IDE for table names. The database and AppTable needs to be re-generated
after every change to the database on anvil.works otherwise your code won't be synced.  This means your test
database on your laptop will be deleted and re-schemed. `yaml2schema.zsh <https://github.com/benlawraus/pyDALAnvilWorks/blob/master/yaml2schema.zsh>`_
does this for you.

FYI, to generate `anvil/tables/AppTables.py`::

    python -m _anvil_designer.generate_apptable



Also depending on your project structure, you might need to do something like::

    try:
        # when running on anvil.works
        from portable_classes import Phone, Email, Contact
    except ImportError:
        # when running on your laptop
        from client_code.portable_classes import Phone, Email, Contact

Yes, this is annoying. Maybe there is a better way...

client_code
^^^^^^^^^^^
For client code tests, the ``_anvil_designer.py`` needs to be generated in the form directory. Every form needs one.
``_anvil_designer`` allows testing on code on the client side (see ``test_ContactForm.py`` for some pytests) and auto-complete on form components.
To generate these, run::

    python -m _anvil_designer.generate_files


or in your test , call::

    from _anvil_designer.generate_files import yaml2class
    class TestYaml2Class:
        def test_init(self):
            yaml2classes()


Note that the included scripts do this for you.

If there is an error, something in your ``yaml`` has not been implemented yet...

User Login/Logout
^^^^^^^^^^^^^^^^^
Tests may fail when run in parallel (pytest) but successfully complete when run individually. To prevent this, save
a unique user in the db for each test and log this user in using::

    anvil.users.force_login(user)

`pyDALAnvilWorks` uses `pytest's env <https://docs.pytest.org/en/latest/example/simple.html#pytest-current-test-env>`_ to
mark the user. At the end of the test, use::

    anvil.users.logout()

See `test_HomeForm.py <https://github.com/benlawraus/pyDALAnvilWorks/blob/master/tests/test_HomeForm.py>`_ for an
example test.

Type Checking
^^^^^^^^^^^^^
It is possible to type check client code using Python 2 style comments and
PyCharm. See `PyCharm type checking <https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html>`_
There is a ``anvil.server.context`` object that could help you with types such as ``Union`` and ``Any``.  Here,
``anvil.server.context.type = "laptop"`` so in your client code (thanks,
`Stefano <https://anvil.works/forum/t/detecting-whether-anvil-is-running-in-the-browser-typing/10975/2?u=ben.lawrence>`_) ::

    if anvil.server.context.type == "laptop":  # for type checking
        from typing import Union
        from .portable_contact import Phone, Email, Location

        texts_to_check = dict()  # type: dict[str, Union[Phone,Email,Location]]



Push Pull Scripts
------------------
In your average day, you will edit code and push and pull your changes to *anvil.works*.
Two scripts are included here to make that easier :
`git_pull_from_anvil_works.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/git_push_to_anvil_works.zsh>`_  and
`git_push_to_anvil_works.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/git_push_to_anvil_works.zsh>`_.
They assume you have your anvil app already git-cloned on your laptop.

The files in the form directories ``_anvil_designer.py`` are (re)generated when you use ``git_pull_from_anvil_works.zsh``.

`yaml2schema.zsh <https://github.com/benlawraus/pyDALAnvilWorks/blob/master/yaml2schema.zsh>`_ is another script
that syncs your laptop database schema from your anvil.works schema. To do this though, the old laptop database
is erased.


Anvil-Extras
--------------
`Anvil-Extras <https://github.com/anvilistas/anvil-extras>`_ is really nice, especially its publish-subscribe module and its
navigation module. So as to use it, there is an ``anvil_extras`` folder here too, but none of its tests or its functionality
have been tested with pyDALAnvilWorks repo.


This project is in its infancy...

Demonstration
--------------

Simple
^^^^^^

This repo has a copy of an anvil.works app already there. So, you can download this repo and run a few commands in your terminal.
Copy and paste what is inside `short_script.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/short_script.zsh>`_ to your mac terminal.


Complicated
^^^^^^^^^^^
But if you want to see how to use your own anvil.works app here, try to understand this `script <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/long_script.zsh>`_.
Copy into your terminal. It will download everything, including this repo.

It will run in your terminal (good for python 3.7+). Before doing, make sure you
create a copy of the example app in your `anvil.works` account.

`CLONE ME <https://anvil.works/build#clone:63HO5XJHHGWRT4ZI=P4WJZJOPX4LOJOMPTTU5XPAT>`_

You need to then substitute your clone example for `myAnvilGit` in the `long_script.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/long_script.zsh>`_. Take a look.

And see some tests in the `tests` directory.


Gotchas
-------

Updating Rows
^^^^^^^^^^^^^^
*anvil.works* allows you update your database using::

    row['name']="Rex Eagle"

This is allowed in this wrapper, with the allowance that no sqlite row will be updated, only the object ``row`` will be
updated. To update the database row, you have to use ``row.update()``

Pytest Fixtures and User login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When running a test, this project uses the process id (PID) of the test to keep track of the user that is logged in.
Logging a user in and out using *PyTest* fixtures may cause the user log in process to use a different PID than
the test, so the test may act as if there is no user logged in. To prevent this, log in the user within the test
and not within a fixture.

Errors during *from client_code.HomeForm import HomeForm*
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
During import, python may run the __init__ of every class. If the class of a form uses an `anvil.users.get_user()`, then
an error will occur because there is no connection to the database. To overcome this, the import has to
occur after the users tables has been initialized. An example is from `test_HomeForm <https://github.com/benlawraus/pyDALAnvilWorks/blob/master/tests/test_HomeForm.py>`_::

    import tests.pydal_def as mydal
    from _anvil_designer.set_up_user import new_user_in_db
    import anvil.users
    from tests.test_app_table import insert_get_contact_row_ref


    def user_login():
        mydal.define_tables_of_db()
        user_ref = new_user_in_db()
        anvil.users.force_login(user_ref)
        user = anvil.users.get_user()
        assert user
        yield user
        anvil.users.logout()


    class TestHomeForm:
        def test_init(self):
            for user in user_login():
                contact_row, contact_ref = insert_get_contact_row_ref(user)
                from client_code.HomeForm import HomeForm
                home_form=HomeForm()
                home_form.contact_form.repeating_panel_2.raise_event("x-contact_name", uid=contact_ref)




Package and Module Forms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the anvil.works, there are package forms and module forms. pyDALAnvilWorks was built to handle package forms.


to be continued....

System
^^^^^^^
This software was developed on an Apple Macbook and has not been tested on anything else.

Thank You
-----------
This work is sponsored by `East Electronics <https://east-elec.com>`_.

