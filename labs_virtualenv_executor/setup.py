import os

from setuptools import setup

if 'VIRTUAL_ENV' in os.environ:
    raise Exception('Run this script outside of a virtualenv!')

setup(
    name='toolness-labs-virtualenv-executor',
    description='Run "labs" within a virtualenv from outside of it.',
    author='Atul Varma',
    author_email='varmaa@gmail.com',
    license='MIT',
    packages=['labs_virtualenv_executor'],
    entry_points = {
        'console_scripts': ['labs=labs_virtualenv_executor:main']
    },
    zip_safe=False,
)
