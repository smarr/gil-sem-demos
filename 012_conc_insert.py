from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success
import sys
import time

# Check whether a loop with len;in can observe non-atomic behavior
# when another thread is running a loop with append;pop;append;pop.


def insert_remove_fn(list):
    for i in range(100_000_000):
        list.append(1)
        list.pop()
        list.append(1)
        list.pop()
    return True


def contains_and_size_fn(list):
    for _ in range(100_000_000):
        l = len(list)
        c = 1 in list
        assert (not c and l == 0) or (
            c and l == 1
        ), f"loop bodies not atomic. length: {l}, element in list: {c}"
    return True


shared_list = []
threads = [
    Thread(insert_remove_fn, (shared_list,)),
    Thread(contains_and_size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
