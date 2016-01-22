from setuptools import setup

setup(
    name='toolness-labs',
    version='0.1',
    description='Command-line tool for labs.toolness.com',
    author='Atul Varma',
    author_email='varmaa@gmail.com',
    license='MIT',
    packages=['labs'],
    entry_points = {
        'console_scripts': ['labs=labs:main']
    },
    zip_safe=False,
)
