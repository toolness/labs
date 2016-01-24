'''
    This module is responsible for running converted
    shelltests.
'''

import doctest
import sys

from . import extraglobs

def run_converted_shelltest(filename):
    '''
    Run the given converted shelltest.

    It is assumed that this function is being run from
    within a container.
    '''

    (failure_count, test_count) = doctest.testfile(
        filename,
        module_relative=False,
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        extraglobs=extraglobs.__dict__
    )
    if failure_count == 0:
        print "Test successful!"
    sys.exit(failure_count)

if __name__ == '__main__':
    run_converted_shelltest(sys.argv[1])
