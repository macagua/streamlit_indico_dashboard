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
    pre-commit install


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


pycodestyle
===========

You can see all options for the script, executing the following command:

::

    python -m pycodestyle --help

Examples of the use:

::

    python -m pycodestyle app.py


isort
=====

You can see all options for the script, executing the following command:

::

    python -m isort --help

Examples of the use:

::

    python -m isort app.py


black
=====

You can see all options for the script, executing the following command:

::

    python -m black --help

Examples of the use:

Check the Python module without made changes it:

::

    python -m black app.py --check

Fix the Python module:

::

    python -m black app.py


pydocstyle
==========

You can see all options for the script, executing the following command:

::

    python -m pydocstyle --help

Examples of the use:

::

    python -m pydocstyle app.py


mypy
====

You can see all options for the script, executing the following command:

::

    python -m mypy --help

Examples of the use:

::

    python -m mypy app.py


bandit
======

You can see all options for the script, executing the following command:

::

    python -m bandit --help

Examples of the use:

::

    python -m bandit -r app.py


wily
====

You can see all options for the script, executing the following command:

::

    python -m wily --help

Build the wily cache
--------------------

::

    python -m wily build app.py

Show metrics for a given file
-----------------------------

Graph test.py against 'loc', 'sloc' and 'comments' (raw operator) metrics:

::

    python -m wily report app.py loc sloc comments --message

Graph a specific metric for a given file
----------------------------------------

Graph a specific metric for a given file, if a path is given, all files
within path will be graphed.

Make a graph *.py files against 'loc' and 'sloc' (raw operator) metrics:

::

    python -m wily graph app.py loc sloc

Make a graph *.py files against 'complexity' (cyclomatic operator) metrics:

::

    python -m wily graph app.py complexity


pre-commit
==========

You can see all options for the script, executing the following command:

::

    pre-commit --help

Examples of the use:

::

    pre-commit run --all-files

Ignore commit verification
--------------------------

::

    git commit --interactive --no-verify
