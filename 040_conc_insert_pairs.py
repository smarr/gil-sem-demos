from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success
import sys
import time

# This is to demonstrate the granularity of the GIL.
# This test is expected to "fail" and report how many tries it took before
# seeing non-atomic loop bodies. The reported number depends on the used
# Python implementation and version.


def insert_fn(list):
    for i in range(100_000_000):
        list.append(1)
        list.append(1)
        list.pop()
        list.pop()
    return True


def size_fn(list):
    for i in range(100_000_000):
        l = len(list)
        assert l % 2 == 0, f"List length was {l} at attempt {i}"
    return True


shared_list = []
threads = [
    Thread(insert_fn, (shared_list,)),
    Thread(size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
