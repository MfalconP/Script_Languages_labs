from datetime import datetime
import sys


# (string host, datetime date_and_time, string metod, string path, string http_version, int kod, int bytes)

# ZADANIE 2 - LISTY I KROTKI
def read_log():
    inputLog = sys.stdin.read()
    logList = list()
    for line in inputLog.split('\n'):
        line = line.split()
        if len(line) == 10:
            logList.append((line[0], datetime.strptime(line[3][1:], "%d/%b/%Y:%H:%M:%S"),
                            line[5][1:], line[6], line[7][:-1], int(line[8]), int(line[9].isdigit() and line[9])))
    return logList


def sort_log(log, index):
    try:
        return sorted(log, key=lambda x: x[index])
    except IndexError:
        print(f"Incorrect index of tuple. Index must be in range: 0-{len(log[0]) - 1}.")


def get_entries_by_addr(log, host):
    newLog = list()
    for request in log:
        if request[0] == host:
            newLog.append(request)
    return newLog


def get_entries_by_code(log, code):
    newLog = list()
    for request in log:
        if request[5] == code:
            newLog.append(request)
    return newLog


def get_failed_reads(log, connect):
    log404 = list()
    log304 = list()
    for request in log:
        if request[5] == 404:
            log404.append(request)
        elif request[5] == 304:
            log304.append(request)
    if connect:
        return log404 + log304
    else:
        return log404, log304


def get_entries_by_extension(log, filetype):
    newLog = list()
    for request in log:
        if request[3][-3:] == filetype:
            newLog.append(request)
    return newLog


def print_entries(log):
    for request in log:
        print(request)


def entry_to_dict(request):
    return {'host': request[0], 'date': request[1], 'method': request[2], 'path': request[3],
            'version': request[4], 'code': request[5], 'bytes': request[6]}


def log_to_dict(log):
    logDict = {}
    for request in log:
        if request[0] not in logDict:
            logDict[request[0]] = [{'date': request[1], 'method': request[2],
                                    'path': request[3], 'version': request[4],
                                    'code': request[5], 'bytes': request[6]}]
        else:
            logDict[request[0]] = logDict[request[0]] + [{'date': request[1], 'method': request[2],
                                                          'path': request[3], 'version': request[4],
                                                          'code': request[5], 'bytes': request[6]}]
    return logDict


def get_addrs(dict_log):
    for key in dict_log.keys():
        print(key)


def print_dict_entry_dates(dict_log):
    for key in dict_log.keys():
        code200num = 0
        for dict in dict_log[key]:
            if dict['code'] == 200:
                code200num += 1
        print(f"{key}:\n"
              f"\trequests amount: {len(dict_log[key])}\n"
              f"\tfirst request date: {dict_log[key][0]['date']}\n"
              f"\tlast request date: {dict_log[key][len(dict_log[key]) - 1]['date']}\n"
              f"\t200 code to all requests: {code200num / len(dict_log[key]):.2f}")


if __name__ == '__main__':
    log_list = read_log()
    sorted_log = sort_log(log_list, 6)
    get_entries_by_addr(log_list, 'unicomp6.unicomp.net')
    get_entries_by_code(log_list, 304)
    get_failed_reads(log_list, True)
    get_entries_by_extension(log_list, 'gif')
    # print_entries(sorted_log)
    entry_to_dict(log_list[0])
    dict_log = log_to_dict(log_list)
    # get_addrs(dict_log)
    print_dict_entry_dates(dict_log)
