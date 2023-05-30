import os
import sys

#  python zad1.py "USER" "IDEA"

env_vars = os.environ

filtered_vars = {}
for arg in sys.argv[1:]:
    for key, value in env_vars.items():
        if arg in key:
            filtered_vars[key] = value

for key, value in sorted(filtered_vars.items()):
    print(key + " : " + value)

