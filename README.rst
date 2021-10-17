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