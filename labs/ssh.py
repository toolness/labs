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

def unix_socket_tunnel(local_port, socket_path):
    d = locals()

    # Note: Ensure that StreamLocalBindUnlink is set to 'yes' and
    # StreamLocalBindMask is set appropriately on SSH_TARGET's
    # sshd_config, or this might not work.

    subprocess.check_call([
        'ssh',
        '-R',
        '%(socket_path)s:127.0.0.1:%(local_port)d' % d,
        SSH_TARGET,
        '-N'
    ])
