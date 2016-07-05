'''

Pipelines - Exercise

This script shows an example on the use of the sys.argv
variable, which collects the UNIX command line parameters
of the script itself.

raise SystemExit

is a command that smoothly exits the script execution.
The use of a try/except structure testing the presence of 
the expected program's parameters is strongly suggested in 
every programs taking parameters from the command line.

'''

import sys

print sys.argv

try:
    filename = sys.argv[1]
except:
    print "Usage: sys_argv.py filename"
    raise SystemExit
else:
    gbk = open(filename)

    for line in gbk:
        if line[0:5] == 'LOCUS':
            print line,
