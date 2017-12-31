#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup

try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip
except (ImportError, ModuleNotFoundError):
    # we need pipenv in order to parse our pipfile
    # since setuptools' setup_requires is broken, we use
    # this vendor hack
    import sys
    import shlex
    import subprocess
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        subprocess.check_output(shlex.split('pip install pipenv -t {}'.format(tempdir)))
        sys.path.append(tempdir)
        from pipenv.project import Project
        from pipenv.utils import convert_deps_to_pip


# get requirements from Pipfile
pfile = Project(chdir=False).parsed_pipfile
default = convert_deps_to_pip(pfile['packages'], r=False)
development = convert_deps_to_pip(pfile['dev-packages'], r=False)


setup(
    install_requires=default,
    tests_require=development,
    extras_require={
        'dev': development,
        'development': development,
        'test': development,
        'testing': development,
    },

    entry_points={
        'console_scripts': [
            'dmp=dmp_cli.cli:main'
        ]
    },

)
