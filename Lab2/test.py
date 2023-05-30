import sys


if __name__ == '__main__':
    text = sys.stdin.read()
    text = text.split("\n")
    for line in text:
        lineSplit = line.split()
        if len(lineSplit) <= 0:
            print(line)
    print("EOF")

