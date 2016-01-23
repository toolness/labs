# Note that this file is executed by setup.py so it shouldn't have any
# external dependencies.

import os

DEFAULT_HOSTNAME = 'labs.toolness.com'

HOSTNAME = os.environ.get('LABS_HOSTNAME', DEFAULT_HOSTNAME)

__version__ = '0.0.1'
