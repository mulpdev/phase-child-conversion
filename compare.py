import sys

if len(sys.argv) < 3:
    sys.stdout.write("usage: .py gene.py-res expected-res\n")
    sys.exit(-1)

mistakes = 0

fnameA = sys.argv[1] #gene.py
fnameB = sys.argv[2] #expected

inA = open(fnameA, 'r')
dataA = inA.read()

inB = open(fnameB, 'r')
dataB = inB.read()

dataA_lines = dataA.split("\n")
dataB_lines = dataB.split("\n")

if len(dataA_lines) != len(dataB_lines):
    print "Input files differ in number of lines"

begin = 6 #this where the first line of algorithm output is not including detailed info

for i in range(begin, len(dataA_lines)):
    #split on ,
    #strip
    #compare

    lineA = dataA_lines[i]
    lineB = dataB_lines[i]

    lineA = lineA.split(',')
    lineB = lineB.split(',')

    for j in range(0, len(lineA)):
        tmpA = lineA[j].strip()
        tmpB = lineB[j].strip()
        
        if tmpA != tmpB:
            print "Error at (%d,%d). -%s- does not match -%s-" %(i, j, tmpA, tmpB)
            mistakes = mistakes + 1

print "\nNOTE: Only the algorithmic output from line %d to %d (counting from 0) was compared" %(begin, len(dataA_lines))

if mistakes == 0:
    print "\nNo differences found!"
