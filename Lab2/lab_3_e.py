def lines200(file):
    lines = list()
    try:
        file = file.split('\n')
        for line in file:
            line = str.rstrip(line)
            lineSplit = line.split()
            if len(lineSplit) > 0:
                code = lineSplit[-2]
                if code == '200':
                    lines.append(line)
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return lines
