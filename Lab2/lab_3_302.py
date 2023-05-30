import lab_3_a_b as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    print("Responds with code 302:", respond.num302(inputText))
