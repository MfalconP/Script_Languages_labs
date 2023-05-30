import csv
from collections import Counter
import sys


file_path = sys.stdin.readline().rstrip()

with open(file_path, 'r') as file:
    contents = file.read()
    char_count = len(contents)
    word_count = len(contents.split())
    line_count = len(contents.splitlines())

    chars_freq = Counter(contents)
    most_common_char = max(chars_freq, key=chars_freq.get)

    words_freq = Counter(contents.split())
    most_common_word = max(words_freq, key=words_freq.get)


results = {
    'file_path': file_path,
    'char_count': char_count,
    'word_count': word_count,
    'line_count': line_count,
    'most_common_char': most_common_char,
    'most_common_word': most_common_word
}

with open('results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([results['file_path'], results['char_count'],
                     results['word_count'], results['line_count'],
                     results['most_common_char'], results['most_common_word']])

