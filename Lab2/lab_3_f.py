import lab_3_e as answ


def times(file):
    text = answ.lines200(file)
    lines = list()
    try:
        for line in text:
            line = str.rstrip(line)
            lineSplit = line.split()
            if len(lineSplit) > 0:
                date = lineSplit[3]
                time = int(date[13:15], 10)
                if time > 22 or time < 6:
                    lines.append(lineSplit[6])
    except(IndexError, TypeError):
        print("Wrong file format!")
    return lines
