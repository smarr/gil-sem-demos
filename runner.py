# This script can run the examples in this repository on different Python executables
# and generates summary output.

import re
import os
import subprocess
import sys
import tokenize
from os import listdir

host_name = os.uname().nodename

# 1. list of python executables to test
PYTHON_EXECUTABLES = (
    [
        "../cpython38/python",
        "../cpython39/python",
        "../cpython310/python",
        "../cpython311/python",
        "../cpython312/python",
        "../cpython313/python",
        "../cpython313-disable-gil/python",
        "../cpython-colesbury-nogil/python",
        "../cpython-colesbury-nogil-latest/python",
        "/data/home/cur/sm951/.local/pypy39/bin/pypy3.9",
        "/data/home/cur/sm951/.local/pypy/bin/pypy3.10",
        "/data/home/cur/sm951/.local/graalpy/bin/graalpy",
    ]
    if "yuria" in host_name
    else [
        "../cpython39/python.exe",
        "../cpython310/python.exe",
        "../cpython311/python.exe",
        "../cpython312/python.exe",
        "../cpython313/python.exe",
        "../pypy3.9-v7.3.13-macos_arm64/bin/pypy3.9",
        "../pypy3.10-v7.3.13-macos_arm64/bin/pypy3.10",
    ]
)

print("GIL Semantics Test Runner")
print("=========================")
print()

print("Testing the following versions:")

# collect version information for the selected Python executables
python_details = {}


class Details:
    def __init__(self, version):
        v = version.split("\n")
        self.version = v[0]
        self.version_complete = version
        self.completed = 0
        self.aborted = 0


for e in PYTHON_EXECUTABLES:
    version = subprocess.run([e, "--version"], capture_output=True)
    version_str = version.stdout.decode("utf-8").strip()
    print("\t", e, "\t", version_str)
    python_details[e] = Details(version_str)

print()


# 2. find all tests

# list all files in current directory, where the name starts with 3 digits, then an underscore,
# and ends with .py
test_files = [f for f in listdir(".") if re.match(r"\d{3}\_.*\.py", f) is not None]
test_files.sort()

if len(sys.argv) > 1:
    test_files = sys.argv[1:]

# 3. for each test
#   - print the name (1st file name, then later descriptive name)


def run_test(e, fn, extra_arg):
    cmd = " ".join([e, fn, extra_arg])
    result = subprocess.run([e, fn, extra_arg], capture_output=True)
    lines = result.stdout.decode("utf-8").strip().split("\n")
    success = lines[-1] == "Completed"
    out = lines[:-1]

    if success:
        print(cmd, "\t", "Completed", "\t", out[0] if len(out) > 0 else "")
        python_details[e].completed += 1
    else:
        err = result.stderr.decode("utf-8").strip().split("\n")
        last_err = err[-1]
        last_err = last_err.replace("AssertionError: ", "")
        print(cmd, "\t", "Aborted", "\t", last_err)
        python_details[e].aborted += 1


def remove_leading_hash(s):
    while s.startswith("#"):
        s = s[1:].strip()
    return s


def extract_main_comment(file_name):
    with tokenize.open(file_name) as f:
        tokens = tokenize.generate_tokens(f.readline)

        comment_not_started = True
        comment_text = []

        for token in tokens:
            if token.type is tokenize.NL:
                continue
            if token.type is tokenize.COMMENT:
                comment_not_started = False
                comment_text.append(remove_leading_hash(token.string))
            else:
                if not comment_not_started:
                    break
        return "\n".join(comment_text)


for file_name in test_files:
    print(file_name)
    print("-" * len(file_name))
    print()

    comment = extract_main_comment(file_name)
    if comment:
        print(comment)
        print()

    for e in PYTHON_EXECUTABLES:
        run_test(e, file_name, "                         ")
        run_test(e, file_name, "--minimal-switch-interval")

    print()


# 4. print summary that shows statistics for each executable

for e in PYTHON_EXECUTABLES:
    print(e, "\t", python_details[e].version)
    print("\t", "Completed:\t", python_details[e].completed)
    print("\t", "Aborted:\t", python_details[e].aborted)
    print()
