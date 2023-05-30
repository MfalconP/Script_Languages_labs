import lab_3_b as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    print('Size of sent data is %.2f GB' % respond.dataSize(inputText))
