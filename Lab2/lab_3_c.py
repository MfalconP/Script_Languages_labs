def largest(file):
    size = 0
    path = ""
    try:
        file = file.split('\n')
        for line in file:
            line = str.rstrip(line)
            line = line.split()
            if len(line) > 0:
                bytesNum = line[-1]
                if bytesNum != '-':
                    if int(bytesNum) > size:
                        size = int(bytesNum)
                        path = line[-4]
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return path, size

