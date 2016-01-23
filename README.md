This is a python package that installs a command-line tool called `labs`,
which makes it easy to do stuff with labs.toolness.com.

## Quick Start

```
virtualenv venv

# On Windows, replace the following line with 'venv\Scripts\activate'.
source venv/bin/activate

python setup.py develop
```

At this point `labs` will be available on your command-line, but only
while your virtualenv is activated. To install it globally:

```
deactivate
cd labs_virtualenv_executor
python setup.py develop
```

You may need to prefix the last command with `sudo`.

This will install a "proxy" `labs` command globally which activates
your virtualenv and then runs the tool within it.

Note that you can avoid the virtualenv stuff entirely by simply
installing the package globally, but this will also install all its
dependencies globally too.

## Running Tests

To run the tests, run:

```
python -m unittest discover
```
