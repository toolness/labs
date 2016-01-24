import sys
import subprocess
import re
import os

def _slugify(s):
    # http://stackoverflow.com/q/5574042/2422398
    slug = s.lower()
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug

def run_in_background(cmdline):
    '''
    Run the given command without waiting for it to complete,  logging
    its output to /var/log/test/.

    We don't care what happens to it because we're in a container that's
    going to be torn down and rebuilt between tests.
    '''

    logfile = open('/var/log/test/%s.log' % _slugify(cmdline), 'w')
    popen = subprocess.Popen(
        cmdline,
        shell=True,
        stdout=logfile,
        stderr=subprocess.STDOUT
    )

def run(cmdline):
    '''
    Run the given command in a shell, waiting for it to complete, and
    outputting its result for doctests to evaluate.
    '''

    try:
        sys.stdout.write(subprocess.check_output(
            cmdline, stderr=subprocess.STDOUT, shell=True
        ))
    except subprocess.CalledProcessError, e:
        # The doctest is already going to fail, so re-raising the exception
        # would just pollute the test output.
        sys.stdout.write('Command %s failed:\n%s' % (repr(cmdline),
                                                     e.output))
