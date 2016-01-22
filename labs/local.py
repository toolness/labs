import subprocess

def call(cmdline, silent=False):
    if not silent:
        print "Calling '%s'..." % ' '.join(cmdline)
    subprocess.check_call(cmdline)
