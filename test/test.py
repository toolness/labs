import doctest
import sys
import os
from subprocess import check_output, STDOUT

def run(cmdline):
    sys.stdout.write(check_output(cmdline, stderr=STDOUT, shell=True))

def run_doctest():
    (failure_count, test_count) = doctest.testfile(
        'doctest.py.txt',
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        extraglobs=dict(run=run, os=os)
    )
    if failure_count == 0:
        print "Test successful!"
    sys.exit(failure_count)

if __name__ == '__main__':
    run_doctest()
