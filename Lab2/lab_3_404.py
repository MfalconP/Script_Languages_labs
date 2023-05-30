import lab_3_a_c as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    print("Responds with code 404:", respond.num404(inputText))
