import os
import argparse
import argh

from . import HOSTNAME, git, ssh, local

MY_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.normpath(os.path.join(MY_DIR, '..'))

def update():
    '''
    Update the CLI.
    '''

    os.chdir(ROOT_DIR)
    local.call(['git', 'pull'])

    # Note that we don't want to use sys.executable here, because we
    # may be being called from labs_virtualenv_executor, so we'll rely
    # on the subshell to find the right python interpreter for us.
    os.system('python setup.py develop')

def main():
    parser = argparse.ArgumentParser(
        description='Tools for %s.' % ssh.HOSTNAME,
    )
    argh.add_commands(parser, [update])
    git.namespace.add_subcommands(parser)
    argh.dispatch(parser)
