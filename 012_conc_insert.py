from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success
import sys
import time

sys.setswitchinterval(0.0000001)


def insert_remove_fn(list):
    for i in range(100_000_000):
        list.append(1)
        time.sleep(0.0)
        list.pop()
    return True


def contains_and_size_fn(list):
    for _ in range(100_000_000):
        l = len(list)
        time.sleep(0.0)
        c = 1 in list
        assert (not c and l == 0) or (c and l == 1)
    return True


shared_list = []
threads = [
    Thread(insert_remove_fn, (shared_list,)),
    Thread(contains_and_size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
