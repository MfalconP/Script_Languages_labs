import re


def read_ssh_logs(filename):
    logs = []
    with open(filename, 'r') as file:
        for line in file:
            log = {}
            # Data and time
            match = re.search(r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})', line)
            if match:
                log['datetime'] = match.group(1)

            # Odczyt hosta
            match = re.search(r'^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+(\w+)', line)
            if match:
                log['host'] = match.group(1)

            # Odczyt PID
            match = re.search(r'\bsshd\[(\d+)\]:', line)
            if match:
                log['pid'] = int(match.group(1))

            # Odczyt adresu IP
            match = re.search(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b', line)
            if match:
                log['ip_address'] = match.group(1)

            # Odczyt nazwy użytkownika
            match = re.search(r'user\s+(\w+)\s+', line)
            if match:
                log['user'] = match.group(1)

            # Odczyt informacji o nieudanej próbie logowania
            match = re.search(r'authentication\s+failure', line)
            if match:
                log['login_success'] = False
            else:
                log['login_success'] = True
            logs.append(log)
    return logs


def get_ipv4s_from_log(log):
    ips = []
    for line in log:
        if 'ip_address' in line:
            ips.append(line['ip_address'])
    return ips


def get_user_from_log(log):
    users = []
    for line in log:
        if 'user' in line:
            users.append(line['user'])
        else:
            users.append('None')
    return users


def get_message_type(filename):
    messages = []
    with open(filename, 'r') as file:
        for line in file:
            if re.search(r"Accepted", line):
                messages.append("udane logowanie")
            elif re.search(r"Failed password", line):
                messages.append("błędne hasło")
            elif re.search(r"Invalid user", line):
                messages.append("błędna nazwa użytkownika")
            elif re.search(r"Disconnected", line):
                messages.append("zamknięcie połączenia")
            elif re.search(r"Failed", line):
                messages.append("nieudane logowanie")
            elif re.search(r"POSSIBLE BREAK-IN ATTEMPT", line):
                messages.append("próba włamania")
            else:
                messages.append("inne")
    return messages


if __name__ == '__main__':
    log = read_ssh_logs("SSH_Lite.log")
    get_ipv4s_from_log(log)
    get_user_from_log(log)
    print(get_message_type("SSH_Lite.log"))
