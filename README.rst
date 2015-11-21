mozio
==============================

This project try to achieve Mozio backend developer Test.

This project Layout is created using cookiecutter-django_

.. _cookiecutter-django: https://github.com/pydanny/cookiecutter-django

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL 9.3 or superior with Postgis Extension

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Then, create a PostgreSQL database and add the database configuration using the  ``dj-database-url`` app pattern: ``postgres://db_owner:password@dbserver_ip:port/db_name`` either:

* in the ``config.settings.common.py`` setting file,
* or in the environment variable ``DATABASE_URL``


You can now run the usual Django ``migrate`` and ``runserver`` command::

    $ python manage.py migrate

    $ python manage.py runserver


How to Use
--------------
To create a **user account**, just go to Sign Up (SignUp_) and fill out the form. Once you submit it.

After being login in, on the navigation bar on the right side are: the Services Areas List (List_) , and Services Area Create (Create_).

In Services Area Create, you can create one clicking on the map to localize markers as vertex of your polygon
service area, map location is based on the user IP, whether is no possible get location, default is based on San Francisco CA,
the coordinates information of each marker(vertex) will be showing on the right side of the page, with the Latitude and Longitude of each one.


In Services Area List you can see if a point is inside a service area clicking on the map, in the right side of the page
you will be notify if the point is or not inside a service area, services areas are loaded from the backend but are not visible.


.. _SignUp: http://ec2-52-33-128-23.us-west-2.compute.amazonaws.com/accounts/signup/
.. _List: http://ec2-52-33-128-23.us-west-2.compute.amazonaws.com/suppliers/service-area/list/
.. _Create: http://ec2-52-33-128-23.us-west-2.compute.amazonaws.com/suppliers/service-area/add/
