import random
import re
import datetime
import statistics
import zad1
from collections import defaultdict


def random_logs_for_user(logfile):
    all_users = zad1.get_user_from_log(zad1.read_ssh_logs(logfile))
    users = []

    for user in all_users:
        if user not in users:
            users.append(user)

    user_id = random.randint(0, len(users)-1)

    user = users[user_id]

    logs = []
    with open(logfile) as f:
        for line in f:
            if user in line:
                logs.append(line.strip())
    return random.sample(logs, random.randint(1, len(logs)))


def analyze_ssh_logs(log_file):
    # regular expressions to extract start and end times of each session
    start_re = re.compile(r'^(\w+\s+\d+ \d+:\d+:\d+) \S+ sshd\[\d+\]: Accepted password for')
    end_re = re.compile(r'^(\w+\s+\d+ \d+:\d+:\d+) \S+ sshd\[\d+\]: (Connection closed|Received disconnect)')

    # list to store duration times
    duration_times = []

    # open log file and read lines
    with open(log_file, 'r') as f:
        lines = f.readlines()

    # iterate over lines and extract start and end times of each session
    start_time = None
    for line in lines:
        if start_re.match(line):
            # found start of session
            start_time = datetime.datetime.strptime(start_re.match(line).group(1), '%b %d %H:%M:%S')
        elif end_re.match(line):
            # found end of session
            end_time = datetime.datetime.strptime(end_re.match(line).group(1), '%b %d %H:%M:%S')
            if start_time is not None and end_time is not None:
                duration_times.append((end_time - start_time).total_seconds())
            start_time = None

    # calculate mean and standard deviation of duration times
    if len(duration_times) > 0:
        mean_duration = datetime.timedelta(seconds=sum(duration_times) / len(duration_times))
        std_dev_duration = datetime.timedelta(seconds=statistics.stdev(duration_times))
    else:
        mean_duration = datetime.timedelta(seconds=0)
        std_dev_duration = datetime.timedelta(seconds=0)

    return mean_duration, std_dev_duration


def analyze_ssh_users(log_file, username):
    # regular expressions to extract start and end times of each session
    start_re = re.compile(r'^(\w+\s+\d+ \d+:\d+:\d+) \S+ sshd\[\d+\]: Accepted password for ' + username)
    end_re = re.compile(r'^(\w+\s+\d+ \d+:\d+:\d+) (\S+ )?sshd\[\d+\]: (Connection closed by|Received disconnect from'
                        r'|pam_unix\(sshd:session\): session closed for user) ' + username)

    # list to store duration times
    duration_times = []

    # open log file and read lines
    with open(log_file, 'r') as f:
        lines = f.readlines()

    # iterate over lines and extract start and end times of each session
    start_time = None
    for line in lines:
        if start_re.match(line):
            # found start of session
            start_time = datetime.datetime.strptime(start_re.match(line).group(1), '%b %d %H:%M:%S')
        elif end_re.match(line):
            # found end of session
            end_time = datetime.datetime.strptime(end_re.match(line).group(1), '%b %d %H:%M:%S')
            if start_time is not None and end_time is not None:
                duration_times.append((end_time - start_time).total_seconds())
            start_time = None

    # calculate mean and standard deviation of duration times
    if len(duration_times) > 0:
        mean_duration = datetime.timedelta(seconds=sum(duration_times) / len(duration_times))
        std_dev_duration = datetime.timedelta(seconds=statistics.stdev(duration_times))
    else:
        mean_duration = datetime.timedelta(seconds=0)
        std_dev_duration = datetime.timedelta(seconds=0)

    return mean_duration, std_dev_duration


def calculate_login_frequency(log_file):
    pattern = r'^(\w+\s+\d+ \d+:\d+:\d+) \S+ sshd\[\d+\]: Accepted password for (\S+)'
    user_frequency = defaultdict(int)

    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                timestamp = match.group(1)
                username = match.group(2)
                user_frequency[username] += 1

    sorted_user_frequency = sorted(user_frequency.items(), key=lambda x: x[1])
    least_frequent_users = [user for user, freq in sorted_user_frequency[:5]]
    most_frequent_users = [user for user, freq in sorted_user_frequency[-5:]][::-1]

    return least_frequent_users, most_frequent_users



if __name__ == '__main__':
    # print(random_logs_for_user("SSH_Lite.log"))
    # print(analyze_ssh_logs('SSH.log'))
    # fztu
    # print(analyze_ssh_users('SSH.log', 'fztu'))
    print (calculate_login_frequency('SSH.log'))

