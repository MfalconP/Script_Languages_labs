import subprocess
import sys


# python restore.py C:\Users\Maryu\.backups


if len(sys.argv) > 1:
    backup_dir = sys.argv[1]

with open(backup_dir + '\\backup_history.csv', 'r') as csvfile:
    data = csvfile.read()

data = data.splitlines()
backupsList = [elem for elem in data if elem != '']
backupsList = backupsList[1:]
backupsList = backupsList[::-1]

print(f'Choose the backup to be restored:')
counter = 1
for backup in backupsList:
    print(f'{counter}. {backup.split(",")[-1]}')
    counter += 1
decision = int(input())

decision_counter = 1
for backup in backupsList:
    if decision_counter == decision:
        restoration_file = backup
    else:
        decision_counter += 1

backup_dir = backup_dir + "\\"
restoration_file = restoration_file.split(',')

powershell_cmd = f'Expand-Archive {backup_dir + restoration_file[-1]} -DestinationPath {restoration_file[1]}'
process = subprocess.Popen(["powershell", "-Command", powershell_cmd], stdout=subprocess.PIPE)
