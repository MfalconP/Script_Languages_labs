import lab_3_c as respond
import sys


if __name__ == '__main__':
    inputText = sys.stdin.read()
    answer = respond.largest(inputText)
    print(f'Size of the largest sent data is {answer[1]} B and its path is {answer[0]}')
