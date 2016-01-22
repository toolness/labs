import subprocess

from . import HOSTNAME

USERNAME = 'varmaa'
SSH_TARGET = '%s@%s' % (USERNAME, HOSTNAME)

def run(cmd):
    subprocess.check_call([
        'ssh',
        SSH_TARGET,
        cmd
    ])
