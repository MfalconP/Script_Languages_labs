import lab_3_g as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    text = respond.friday(inputText)
    for line in text:
        print(line)
