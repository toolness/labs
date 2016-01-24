import doctest
import sys

from . import extraglobs

def run_converted_shelltest(filename):
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
