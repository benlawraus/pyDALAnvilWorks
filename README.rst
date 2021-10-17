What is it?
------------
Python programs to allow you to use any database while testing your `anvil.works <https://anvil.works>`_ app.

How is it done?
---------------
The program uses `pyDAL <https://py4web.com/_documentation/static/en/chapter-07.html>`_ to substitute
the database interactions. This means you can git clone your app on your laptop and run some tests on it without
modifying your app or using the external server's database.

How to use it?
---------------
Copy the directory structure into your cloned anvil.works app. Instead of calling the anvil.works routines, it will use
the local version instead.

Of course, you will need a complete mirror of your anvil.works external database. To set that up,
use this `converter <https://github.com/benlawraus/useAnvilYaml>`_. In your cloned anvil.works
app, there is a file called `anvil.yaml`. This file contains a description of your
database schema. The `converter <https://github.com/benlawraus/useAnvilYaml>`_ will read
the `anvil.yaml` and generate a `pyDAL <https://py4web.com/_documentation/static/en/chapter-07.html>`_
definition file (`pydal_def.py`) that you can use to run your tests.

Examples
---------
See the tests in the `tests` directory.