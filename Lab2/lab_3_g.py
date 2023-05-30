import lab_3_e as answ
from datetime import datetime


def friday(file):
    text = answ.lines200(file)
    lines = list()
    try:
        for line in text:
            line = str.rstrip(line)
            lineSplit = line.split()
            if len(lineSplit) > 0:
                date = lineSplit[3]
                date = date[1:12]
                date = datetime.strptime(date, '%d/%b/%Y')
                day = date.weekday()
                if day == 4:
                    lines.append(lineSplit[6])
    except(IndexError, TypeError):
        print("Wrong file format!")
    return lines
