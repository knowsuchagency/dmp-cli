=======
dmp-cli
=======


.. image:: https://img.shields.io/pypi/v/dmp-cli.svg
        :target: https://pypi.python.org/pypi/dmp-cli

.. image:: https://img.shields.io/travis/knowsuchagency/dmp-cli.svg
        :target: https://travis-ci.org/knowsuchagency/dmp-cli

.. image:: https://pyup.io/repos/github/knowsuchagency/dmp-cli/shield.svg
     :target: https://pyup.io/repos/github/knowsuchagency/dmp-cli/
     :alt: Updates

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg



A command-line-interface for `django-mako-plus`_.


* Documentation: https://knowsuchagency.github.io/dmp-cli
* Source: https://github.com/knowsuchagency/dmp-cli


Installation
------------

::

    pipenv install -d dmp-cli
    # or
    pip install dmp-cli

Usage
---------

To create a new `django-mako-plus`_ project use

::

    dmp new project [NAME]

Similarly, for new apps

::

    dmp new app [NAME]

These are just shortcuts for

::

    python3 -m django startproject --template=http://cdn.rawgit.com/doconix/django-mako-plus/master/project_template.zip [NAME]
    # and
    python3 manage.py startapp --template=http://cdn.rawgit.com/doconix/django-mako-plus/master/app_template.zip --extension=py,htm,html [NAME]

... but use the templates on your local filesystem from the currently installed version of `DMP`_, rather than fetching the templates from github.

.. _`django-mako-plus`: http://django-mako-plus.readthedocs.io/
.. _`DMP`: http://django-mako-plus.readthedocs.io/
