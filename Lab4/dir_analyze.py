import csv
import os
import subprocess
import sys

analyze_script = "file_analyze.py"
# python dir_analyze.py
files_dir = sys.argv[1]
files = [os.path.join(files_dir, file) for file in os.listdir(files_dir) if file.endswith(".txt")]
result = list()

for file in files:
    process = subprocess.Popen(['python', 'file_analyze.py'], stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.communicate(file)

    with open('results.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        answer = next(reader)
        dict_answer = {'path': answer[0],
                       'chars_num': answer[1],
                       'words_num': answer[2],
                       'lines_num': answer[3],
                       'most_common_char': answer[4],
                       'most_common_word': answer[5]
                       }
        result.append(dict_answer)


files_num = len(result)
chars_num = 0
words_num = 0
lines_num = 0
most_common_chars = list()
most_common_words = list()

for answ in result:
    chars_num += int(answ['chars_num'])
    words_num += int(answ['words_num'])
    lines_num += int(answ['lines_num'])
    most_common_chars.append(answ['most_common_char'])
    most_common_words.append(answ['most_common_word'])

print(f'Files number {files_num}\n'
      f'Chars number {chars_num}\n'
      f'Words number {words_num}\n'
      f'Lines number {lines_num}\n'
      f'Most common chars: {most_common_chars}\n'
      f'Most common words: {most_common_words}')

