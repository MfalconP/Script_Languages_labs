import os
import subprocess
import datetime
import csv
import sys

dirname = sys.argv[1]
dirname = dirname.replace('\\', '\\\\')

backup_dir = os.path.expanduser('~\.backups')
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir)

timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
dir_name_format = dirname.split('\\\\')
filename = f"{timestamp}-{dir_name_format[-1]}.zip"

backup_dir_with_zip = 'C:\\Users\\Maryu\\.backups\\' + filename

powershell_cmd = f'Compress-Archive -Path {dirname} -DestinationPath {backup_dir_with_zip}'
process = subprocess.Popen(["powershell", "-Command", powershell_cmd], stdout=subprocess.PIPE)

backup_history_path = os.path.join(backup_dir, 'backup_history.csv')
header = ['Data wykonania', 'Lokalizacja katalogu', 'Nazwa pliku']
backup_info = [timestamp, dirname, filename]

if os.path.exists(backup_history_path):
    with open(backup_history_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(backup_info)
else:
    with open(backup_history_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(backup_info)

print(f"Utworzono kopię zapasową {dirname} jako {filename}.")
