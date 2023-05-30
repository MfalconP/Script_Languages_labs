def dataSize(file):
    size = 0
    try:
        file = file.split('\n')
        for line in file:
            line = str.rstrip(line)
            line = line.split()
            if len(line) > 0:
                bytesNum = line[-1]
                if bytesNum != '-':
                    size += int(bytesNum)
    except(ValueError, IndexError, TypeError):
        print("Wrong file format!")
    return size/1000000000
