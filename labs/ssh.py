import subprocess

from . import HOSTNAME

USERNAME = 'varmaa'
SSH_TARGET = '%s@%s' % (USERNAME, HOSTNAME)

def run(cmd, silent=False):
    if not silent:
        print("Running '%s' on %s..." % (cmd, SSH_TARGET))
    subprocess.check_call([
        'ssh',
        SSH_TARGET,
        cmd
    ])
