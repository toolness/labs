import os

from setuptools import setup

INIT_PY = os.path.join('labs', '__init__.py')

# Get constants from __init__.py w/o importing it.
exec(compile(open(INIT_PY).read(), INIT_PY, 'exec'))

setup(
    name='toolness-labs',
    version=__version__,
    description='Command-line tool for %s' % HOSTNAME,
    author='Atul Varma',
    author_email='varmaa@gmail.com',
    license='MIT',
    install_requires=[
        'argh',
    ],
    packages=['labs'],
    entry_points = {
        'console_scripts': ['labs=labs.script:main']
    },
    zip_safe=False,
)
