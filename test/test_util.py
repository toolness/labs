import doctest
import sys
from os import mkdir, chdir
from subprocess import check_output
from functools import partial

def run(cmdline):
    sys.stdout.write(check_output(cmdline, shell=True))

def run_doctest():
    (failure_count, test_count) = doctest.testfile(
        'doctest.txt',
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        extraglobs=globals()
    )
    if failure_count == 0:
        print "Test successful!"
    sys.exit(failure_count)

if __name__ == '__main__':
    run_doctest()
