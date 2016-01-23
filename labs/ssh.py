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

def tunnel(local_port, remote_port, remote_bind_address=''):
    d = locals()
    subprocess.check_call([
        'ssh',
        '-R',
        '%(remote_bind_address)s:%(remote_port)d:127.0.0.1:%(local_port)d' % d,
        SSH_TARGET,
        '-N'
    ])
