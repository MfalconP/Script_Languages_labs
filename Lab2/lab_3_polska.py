import lab_3_h as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    text = respond.polska(inputText)
    for line in text:
        print(line)
