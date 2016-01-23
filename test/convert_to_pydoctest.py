def convert_to_pydoctest():
    outfile = open('doctest.py.txt', 'w')
    for line in open('doctest.txt'):
        if line.startswith('    $ '):
            cmdline = line[6:].strip()
            if cmdline.startswith('cd '):
                funcname = 'os.chdir'
                cmdline = cmdline[3:]
            else:
                funcname = 'run'
            line = "    >>> %s('%s')\n" % (funcname, cmdline)
        outfile.write(line)

if __name__ == '__main__':
    convert_to_pydoctest()
