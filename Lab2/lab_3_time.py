import lab_3_f as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    text = respond.times(inputText)
    for line in text:
        print(line)
