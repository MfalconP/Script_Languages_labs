def polska(file):
    lines = list()
    try:
        file = file.split('\n')
        for line in file:
            lineSplit = line.split()
            if len(lineSplit) > 0:
                host = lineSplit[0]
                if '.pl' == host[-3:]:
                    lines.append(line)
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return lines
