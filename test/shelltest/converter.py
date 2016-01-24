'''
    This module is responsible for converting shelltest
    files to doctest files.

    For example, most lines convert to run() calls:

        >>> convert_line('    $ ls')
        "    >>> run('ls')"

    But sometimes we want to run commands in the background,
    which we can do with a special comment:

        >>> convert_line('    $ run-server     # Keep this running.')
        "    >>> run_in_background('run-server     # Keep this running.')"

    And sometimes we want to change directories, which needs to be
    done in-process:

        >>> convert_line('    $ cd blah')
        "    >>> os.chdir('blah')"
'''

def convert_line(line):
    return convert_lines([line])[0][:-1]

def convert_lines(lines):
    return [line for line in iter_convert_lines(lines)]

def iter_convert_lines(lines):
    for line in lines:
        if line.startswith('    $ '):
            cmdline = line[6:].strip()
            if cmdline.startswith('cd '):
                funcname = 'os.chdir'
                cmdline = cmdline[3:]
            elif cmdline.endswith('# Keep this running.'):
                funcname = 'run_in_background'
            else:
                funcname = 'run'
            line = "    >>> %s('%s')\n" % (funcname, cmdline)
        yield line

def convert_file(src_file, dest_file):
    outfile = open(dest_file, 'w')
    for line in iter_convert_lines(open(src_file)):
        outfile.write(line)
