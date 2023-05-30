def num302(file):
    num = 0
    try:
        file = file.split('\n')
        for line in file:
            line = str.rstrip(line)
            line = line.split()
            if len(line) > 0:
                code = line[-2]
                if code == '302':
                    num += 1
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return num
