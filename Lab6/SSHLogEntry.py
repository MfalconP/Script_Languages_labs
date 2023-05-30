from ipaddress import IPv4Address
from datetime import datetime
import re
from abc import ABC, abstractmethod


class SSHLogEntry(ABC):
    def __init__(self, log_line):
        time = re.search(r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})', log_line)
        self.timestamp = datetime.strptime(time.group(1), '%b %d %H:%M:%S')

        host = re.search(r'^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+(\w+)', log_line)
        self.hostname = host.group(1)

        line_splt = log_line.split()
        self.__raw_message = ' '.join(line_splt[5:])

        pid = re.search(r'\bsshd\[(\d+)\]:', log_line)
        self.pid = int(pid.group(1))

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} {self.hostname} {self.pid} {self.__raw_message} "

    def __repr__(self):
        return f"SSHLogEntry(log_line='{self.__str__()}')"

    def __eq__(self, other):
        if not isinstance(other, SSHLogEntry):
            return False
        return self.timestamp == other.timestamp \
            and self.hostname == other.hostname \
            and self.pid == other.pid \
            and self.__raw_message == other.__raw_message

    def __lt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object.")
        return self.timestamp < other.timestamp

    def __gt__(self, other):
        if not isinstance(other, SSHLogEntry):
            raise TypeError("Cannot compare SSHLogEntry with non-SSHLogEntry object.")
        return self.timestamp > other.timestamp

    def get_ipv4_address(self):
        ip = re.search(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b', self.__raw_message)
        if ip:
            return IPv4Address(ip.group(1))
        else:
            return None

    @abstractmethod
    def validate(self):
        pass

    @property
    def has_ip(self):
        return self.get_ipv4_address() is not None

    def get_raw_msg(self):
        return self.__raw_message


class FailedPasswd(SSHLogEntry):
    def __init__(self, log_line):
        super().__init__(log_line)
        self.user = None
        self.port = None

        raw_msg = self.get_raw_msg().split()

        if 'invalid user' in self.get_raw_msg():
            self.user = raw_msg[5]
        else:
            self.user = 'root'

        self.port = int(raw_msg[-2])

    def validate(self):
        if not self.user or not self.port:
            return False

        return True


class AcceptedPasswd(SSHLogEntry):
    def __init__(self, log_line):
        super().__init__(log_line)
        self.user = None
        self.port = None

        raw_msg = self.get_raw_msg().split()
        self.user = raw_msg[3]
        self.port = int(raw_msg[-2])

    def validate(self):
        if not self.user or not self.port:
            return False
        return True


class Error(SSHLogEntry):
    def __init__(self, log_line):
        super().__init__(log_line)
        self.type = re.search(r":\s(.+)", log_line).group(1)

    def validate(self):
        if not self.type:
            return False
        return True


class Other(SSHLogEntry):
    def __init__(self, log_line):
        super().__init__(log_line)

    def validate(self):
        return True


class SSHLogJournal:
    def __init__(self):
        self.entries = []

    def append(self, log_line):
        if 'Failed password' in log_line:
            obj = FailedPasswd(log_line)
        elif 'error' in log_line:
            obj = Error(log_line)
        elif 'Accepted password' in log_line:
            obj = AcceptedPasswd(log_line)
        else:
            obj = Other(log_line)
        obj.validate()
        self.entries.append(obj)

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __contains__(self, item):
        return item in self.entries

    def filter_by_date(self, start_date, end_date):
        filtered_entries = []
        for entry in self.entries:
            if start_date <= entry.timestamp <= end_date:
                filtered_entries.append(entry)
        return filtered_entries

    def filter_by_ip(self, ip_address):
        filtered_entries = []
        for entry in self.entries:
            if entry.get_ipv4_address() == ip_address:
                filtered_entries.append(entry)
        return filtered_entries


class SSHUser:
    def __init__(self, username: str, last_login: datetime):
        self.username = username
        self.last_login = last_login

    def validate(self):
        if str(self.username) == r'^[a-z_][a-z0-9_-]{0,31}$':
            raise ValueError("Username is incorrect")


if __name__ == '__main__':
    journal = SSHLogJournal()
    with open('SSH_Lite.log', 'r') as log:
        for line in log:
            journal.append(line)

    users = []
    for entry in journal:
        msg = entry.get_raw_msg()
        match = re.search(r'user\s+(\w+)\s+', msg)
        if match and match.group(1) not in [user.username for user in users]:
            user = SSHUser(match.group(1), entry.timestamp)
            try:
                user.validate()
                users.append(user)
            except ValueError as e:
                print(f"Error creating user {match.group(1)}: {str(e)}")

    for user in users:
        try:
            user.validate()
            print(f"{user.username} is valid")
        except ValueError as e:
            print(f"Error validating user {user.username}: {str(e)}")

