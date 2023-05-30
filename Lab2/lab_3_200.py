import lab_3_a_a as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    print("Responds with code 200:", respond.num200(inputText))
