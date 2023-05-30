import sys

with open(sys.argv[1], 'r') as inputFile:
    for line in inputFile:
        line = line.rstrip()
        print(line)
