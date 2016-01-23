import doctest
import sys
import os
from subprocess import check_output, STDOUT, CalledProcessError

def run(cmdline):
    try:
        sys.stdout.write(check_output(cmdline, stderr=STDOUT, shell=True))
    except CalledProcessError, e:
        sys.stdout.write('Command %s failed:\n%s' % (repr(cmdline),
                                                     e.output))

def run_doctest(filename):
    (failure_count, test_count) = doctest.testfile(
        filename,
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        extraglobs=dict(run=run, os=os)
    )
    if failure_count == 0:
        print "Test successful!"
    sys.exit(failure_count)

if __name__ == '__main__':
    run_doctest(sys.argv[1])
