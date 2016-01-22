import subprocess

from .cmdline import Namespace
from . import ssh

ORIGIN = 'labs'
GIT_DIR = 'git'
BASE_SSH_TARGET = ssh.SSH_TARGET + ':' + GIT_DIR + '/'

namespace = Namespace('git', dict(
    title='git-related commands'
))

@namespace
def list():
    '''
    List git repositories
    '''

    ssh.run('ls %s' % GIT_DIR)

@namespace
def clone(repository):
    '''
    Clone the given repository.
    '''

    subprocess.check_call(['git', 'clone', BASE_SSH_TARGET + repository,
                           '--origin', ORIGIN])
