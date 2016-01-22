import posixpath

from .cmdline import Namespace
from . import ssh, local

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

    ssh.run('ls %s' % GIT_DIR, silent=True)

@namespace
def destroy(repository):
    '''
    Destroy a remote repository.
    '''

    ssh.run('rm -rf %s' % posixpath.join(GIT_DIR, repository))

@namespace
def create(repository):
    '''
    Create a new repository and add it as a git remote.
    '''

    remote_dirname = posixpath.join(GIT_DIR, repository)
    ssh_target = BASE_SSH_TARGET + repository

    print("Creating remote repository.")

    ssh.run('mkdir %(remote_dirname)s && git -C %(remote_dirname)s '
            'init --bare' % locals())

    local.call(['git', 'remote', 'add', 'labs', ssh_target])

@namespace
def clone(repository):
    '''
    Clone the given repository.
    '''

    local.call(['git', 'clone', BASE_SSH_TARGET + repository,
                '--origin', ORIGIN])
