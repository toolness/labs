import os
import sys

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_VENV_DIR = os.path.normpath(os.path.join(ROOT_DIR, '..', '..', 'venv'))

def get_venv_bin_dir():
    venv_dir = os.path.join(ROOT_VENV_DIR, 'Scripts')
    if not os.path.exists(venv_dir):
        venv_dir = os.path.join(ROOT_VENV_DIR, 'bin')
    if not os.path.exists(venv_dir):
        raise Exception('Expected to find a virtualenv in %s' % ROOT_VENV_DIR)
    return venv_dir

def main():
    # https://virtualenv.pypa.io/en/latest/userguide.html
    activate_this = os.path.join(get_venv_bin_dir(), 'activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))

    import labs.script
    labs.script.main()
