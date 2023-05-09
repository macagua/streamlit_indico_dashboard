========================
DEVELOPMENT ENVIRONMENTS
========================


Pre-requirements
================

Pre requirements dependencies:

::

    sudo apt-get update
    sudo apt-get install build-essential pkg-config python3-dev
    virtualenv venv
    source venv/bin/activate
    pip install -U pip
    pip install -r requirements/dev.txt


flake8
======

You can see all options for the script, executing the following command:

::

    python -m flake8 --help

Examples of the use:

::

    python -m flake8 app.py


pylint
======

You can see all options for the script, executing the following command:

::

    python -m pylint --help

Examples of the use:

::

    python -m pylint app.py

Examples of the use for disable some check messages:

::

    python -m pylint --disable=C0103,W0511 app.py
