import tkinter as tk
from tkinter import filedialog
from datetime import datetime


# (string host, datetime date_and_time, string metod, string path, string http_version, int kod, int bytes)
def analyze_log(logfile):
    logList = list()
    with open(logfile) as file:
        for line in file:
            line = line.split()
            if len(line) == 10:
                logList.append({
                    'host': line[0],
                    'datetime': datetime.strptime(line[3][1:], "%d/%b/%Y:%H:%M:%S"),
                    'method': line[5][1:],
                    'path': line[6],
                    'http_version': line[7][:-1],
                    'code': int(line[8]),
                    'size': int(line[9].isdigit() and line[9])
                })
        return logList


def read_log(logfile):
    logList = list()
    with open(logfile) as file:
        for line in file:
            logList.append(line)
        return logList


