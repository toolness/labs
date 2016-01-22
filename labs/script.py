import argparse
import argh

from . import HOSTNAME, git, ssh

def main():
    parser = argparse.ArgumentParser(
        description='Tools for %s.' % ssh.HOSTNAME,
    )
    git.namespace.add_subcommands(parser)
    argh.dispatch(parser)
