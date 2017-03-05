# Note that this file is executed by setup.py so it shouldn't have any
# external dependencies.

import os

DEFAULT_HOSTNAME = 'labs.toolness.com'

DEFAULT_HTTPS_TUNNEL_HOSTNAME = 'tunnel.toolness.org'

DEFAULT_HTTPS_TUNNEL_PATH = '/tmp/tunnel/tunnel.sock'

HOSTNAME = os.environ.get('LABS_HOSTNAME', DEFAULT_HOSTNAME)

HTTPS_TUNNEL_HOSTNAME = os.environ.get('LABS_HTTPS_TUNNEL_HOSTNAME',
                                       DEFAULT_HTTPS_TUNNEL_HOSTNAME)

HTTPS_TUNNEL_PATH = os.environ.get('LABS_HTTPS_TUNNEL_PATH',
                                   DEFAULT_HTTPS_TUNNEL_PATH)

__version__ = '0.0.1'
