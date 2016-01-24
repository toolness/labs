def convert_lines(lines):
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

def convert_to_pydoctest(src_file, dest_file):
    outfile = open(dest_file, 'w')
    for line in convert_lines(open(src_file)):
        outfile.write(line)
