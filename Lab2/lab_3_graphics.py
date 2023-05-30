import lab_3_d as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    print(f'Graphics to other sent data is  {respond.graphics(inputText):.3f} ')
