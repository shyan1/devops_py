# Use the `open` function to create a file object that can read and write files.

file_path = 'bookofdreams.txt'
# file = open(file_path, 'r')     # default mode is 'rt' (read and text mode)

with open(file_path, 'rt') as file:
    content = file.read()
    print(len(content))

# `readlines`
file = open(file_path, 'r')
text = file.readlines()
print(len(text))
print(text[1])
file.close()

#
text = """export STAGE=PROD
export TABLE_ID=token-storage-1234"""

with open('.envrc', 'w') as opened_file:
    opened_file.write(text)

#
import pathlib

# pathlib.Path("some_files_path").read_bytes()
# pathlib.Path("").read_text()
# pathlib.Path("").write_bytes()
# pathlib.Path("").write_text(data)

# json
import json
from pprint import pprint

with open('service-policy.json', 'r') as opened_file:
    policy = json.load(opened_file)
    pprint(policy)

# The `pprint` module automatically formats Python objects for printing.
# Its output is often more easily read and is a handy way of looking at nested data structures

# use `json.dump` to write a Python dictionary as a JSON file.
# json.dump(text, opened_file)

# YAML
import yaml

with open('verify-apache.yml', 'r') as opened_file:
    verify_apache = yaml.safe_load(opened_file)
    pprint(verify_apache)

#
# yaml.dump(text, opened_file)

# CSV
import csv

with open('registered_user_count_ytd.csv', 'r') as csv_file:
    off_reader = csv.reader(csv_file, delimiter=',')
    for _ in range(5):
        pprint(next(off_reader))

# pandas.DataFrame
import pandas as pd

df = pd.read_csv('registered_user_count_ytd.csv')

print(type(df))
print(df)
print(df.head(3))
print(df.describe())

# Common Log Format (CLF)
# <IP Address> <Client Id> <User Id> <Time> <Request> <Status> <Size>
#
import re
line = '127.0.0.1 - rj [13/Nov/2019:14:43:30] "GET HTTP/1.0" 200'
matched = re.search(r'(?P<IP>\d+\.\d+\.\d+\.\d+)', line)
print(matched)
print(matched.group("IP"))

r = r'(?P<IP>\d+\.\d+\.\d+\.\d+)'
r += r' - (?P<User>\w+) '
r += r'\[(?P<Time>\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
r += r' (?P<Request>".+")'

m = re.search(r, line)
print(m)
print(m.group("IP"))
print(m.group("User"))
print(m.group("Time"))
print(m.group("Request"))

# Windows:      \r\n
# Linux-based:  \n
# Python handles the line-ending translation
with open('big-data.txt', 'r') as source_file:
    with open('big-data-corrected.txt', 'w') as target_file:
        for line in source_file.readlines():
            target_file.write(line)


def line_reader(file_path):
    with open(file_path, 'r') as source_file:
        for line in source_file.readlines():
            yield line


reader = line_reader('big-data.txt')

with open('big-data-corrected.txt', 'w') as target_file:
    for line in reader:
        target_file.write(line)


# If you do not or cannot use line endings as a means of breaking up your data, as in the
# case of a large binary file, you can read your data in chunks.
# You pass the number of bytes read in each chunk to the file objects 'read' method
def binary_file_reader(file_path):
    with open(file_path, 'rb') as source_file:
        while True:
            chunk = source_file.read(1024)
            if chunk:
                yield chunk
            else:
                break


print(binary_file_reader('stars-2-720x1280.jpg'))

#
#
# The `os` module
#
# The `os` module handles many low-level operating system calls and attempts to offer a
# consistent interface across multiple operating system.
#
import os

# os.listdir
# os.rename(src, dst)
# os.chmod('file_path', 0o777)
# os.mkdir
# os.makedirs
# os.remove(file_path)
# os.removedirs('')
# os.stat()     # Get stats about the file or directory.

cur_dir = os.getcwd()
print(cur_dir)

print(os.path.split(cur_dir))
print(os.path.dirname(cur_dir))  # same as os.path.split(cur_dir)[0]
print(os.path.basename(cur_dir))

while os.path.basename(cur_dir):
    print(cur_dir)
    cur_dir = os.path.dirname(cur_dir)

#
home_dir = os.path.expanduser("~")


def find_rc(rc_name=".examplerc"):
    # Check for ENV variable
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}", rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        if os.path.exists(config_path):
            return config_path

    # Check the current working directory
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check user home directory
    config_path = os.path.join(os.path.expanduser("~"), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check direcotory of this file
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")


# os.walk
def walk_path(parent_path):
    for root, dirs, files in os.walk(parent_path):
        print(f"Checking: {parent_path}")
        for file_name in files:
            file_path = os.path.join(parent_path, file_name)
            last_access = os.path.getatime(file_path)
            size = os.path.getsize(file_path)
            print(f"File: {file_path}")
            print(f"\tlast accessed: {last_access}")
            print(f"\tsize: {size}")


# file_rc
def find_rc(rc_name=".examplerc"):
    # Check for env variable
    var_name = "EXAMPLERC_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_posix()
    # Check the current working directory
    config_path = pathlib.Path.cwd() / rc_name
    if config_path.exists():
        return config_path.as_posix()

    # Check the user home directory
    config_path = pathlib.Path.home() / rc_name
    if config_path.exists():
        return config_path.as_posix()

    # Check the direcotory of this file
    file_path = pathlib.Path(__file__).resolve()
    config_path = file_path.parent / rc_name
    if config_path.exists():
        return config_path.as_posix()

    print(f"File {rc_name} not found")