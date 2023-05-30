import os
import sys


path_var = os.getenv('PATH')

path_dirs = path_var.split(os.pathsep)
command_params = sys.argv[1:]

if 'dirs' in command_params:
    for path_dir in path_dirs:
        print(path_dir)

if 'executables' in command_params:
    for path_dir in path_dirs:
        print(f"{path_dir}:")
        for file_name in os.listdir(path_dir):
            file_path = os.path.join(path_dir, file_name)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                print(f" - {file_name}")

