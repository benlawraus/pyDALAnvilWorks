What is it?
------------
To allow you to:
    * Use any database while testing your `anvil.works <https://anvil.works>`_ app.
    * Create and run tests using pytest. These tests would be for the python in client_side forms, as well as server_side python. No testing of javascript UI can be done here.
    * Most importantly: use **PyCharm** more with auto-complete on forms.


Recent Changes
---------------

..  csv-table::
    :header: "Before","Now"

    "``_anvil_designer.py`` generated when you first call its Form","the files are all generated for all forms at once."



How is it done?
---------------
The program uses `pyDAL <https://github.com/web2py/pydal>`_ to substitute
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
the `anvil.yaml` and generate a `pyDAL <https://github.com/web2py/pydal>`_
definition file (`pydal_def.py`) that you can use to run your tests. Place `pydal_def.py` into your
`tests` directory.

Also create a `database` directory there to put all your database files.

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

server_code
^^^^^^^^^^^^
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

client_code
^^^^^^^^^^^
For client code tests, the ``_anvil_designer.py`` needs to generated in the form directory. Every form needs one.
``_anvil_designer`` allows testing on code on the client side (see ``test_ContactForm.py`` for some pytests) and auto-complete on form components.
To generate these, run::

    python -m _anvil_designer.generate_files


or in your test , call::

    from _anvil_designer.generate_files import yaml2class
    class TestYaml2Class:
        def test_init(self):
            yaml2class()


If there is an error, what you have in your ``yaml`` has not been implemented yet...

Push Pull Scripts
------------------
In your average day, you will edit code and push and pull your changes to *anvil.works*.
Two scripts are included here to make that easier : ``git_pull_from_anvil_works.zsh`` and ``git_push_to_anvil_works.zsh``.
They assume you have your anvil app already git-cloned on your laptop.

The files in the form directories ``_anvil_designer.py`` are (re)generated when you use ``git_pull_from_anvil_works.zsh``.

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

This repo has a copy of an anvil.works app already there. So, you can download this repo and run a few commands in your terminal.
Copy and paste `short_script.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/short_script.zsh>`_ to do that.


Complicated
^^^^^^^^^^^
But if you want to see how to use your own anvil.works app here, try to understand this `script <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/long_script.zsh>`_.

It will run in your terminal (good for python 3.7+). Before doing, make sure you
create a copy of the example app in your `anvil.works` account.

`CLONE ME <https://anvil.works/build#clone:XWM5WQ66ONSRYYXL=WJUZGODLYP2JSYWR3XU2Y2XD>`_

You need to then substitute your clone example for `myAnvilGit` in the `long_script.zsh <https://raw.githubusercontent.com/benlawraus/pyDALAnvilWorks/master/long_script.zsh>`_. Take a look.

And see some tests in the `tests` directory.

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

This is allowed in this wrapper, with the allowance that no sqlite row will be updated, only the object ``row`` will be
updated. To update the database row, you have to use ``row.update()``

Package and Module Forms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the anvil.works, there are package forms and module forms. pyDALAnvilWorks was built to handle package forms.


to be continued....


Thank You
-----------
This work is sponsored by `East Electronics <https://east-elec.com>`_.

