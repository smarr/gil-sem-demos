# This script can run the examples in this repository on different Python executables
# and generates summary output.

import re
import subprocess
from os import listdir


# 1. list of python executables to test
PYTHON_EXECUTABLES = [
    "../cpython39/python.exe",
    # "../cpython310/python.exe",
    "../cpython311/python.exe",
    # "../cpython312/python.exe",
    # "../cpython313/python.exe",
    "../pypy3.9-v7.3.13-macos_arm64/bin/pypy3.9",
    "../pypy3.10-v7.3.13-macos_arm64/bin/pypy3.10",
]

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
        self.failed = 0


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
        print(cmd, "\t", "Failed", "\t", last_err)
        python_details[e].failed += 1


for fn in test_files:
    print(fn)
    print("-" * len(fn))
    print()

    for e in PYTHON_EXECUTABLES:
        run_test(e, fn, "                         ")
        run_test(e, fn, "--minimal-switch-interval")

    print()


# 4. print summary that shows how many tests failed for each executable

for e in PYTHON_EXECUTABLES:
    print(e, "\t", python_details[e].version)
    print("\t", "Completed:", python_details[e].completed)
    print("\t", "Failed:", python_details[e].failed)
    print()
