import os

inputfile = './1.py'
outfile = './test.txt'

with open(inputfile, 'r') as inp, open(outfile, 'w') as op:
    i = 0
    for line in inp:
        print line
        line = `i` + ' ' + line
        op.write(line)
        i = i + 1

with open(inputfile, 'r') as inp, open(outfile, 'w') as op:
    i = 0
    line = inp.read()
    print line