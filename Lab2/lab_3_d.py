def graphics(file):
    totalNumb = 0
    graphicsNumb = 0
    try:
        file = file.split('\n')
        for line in file:
            line = str.rstrip(line)
            line = line.split()
            if len(line) > 0:
                if line[-2] == '200':
                    totalNumb += 1
                    if '.gif' in line[-4] or '.jpeg' in line[-4] or '.jpg' in line[-4] or '.xbm' in line[-4]:
                        graphicsNumb += 1
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return graphicsNumb/totalNumb
