from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success

# This is to demonstrate the granularity of the GIL.
# This test is expected to "fail" and report how many tries it took before
# seeing non-atomic loop bodies. The reported number depends on the used
# Python implementation and version.


def append(l):
    l.append(1)
    l.append(1)


def remove(l):
    l.pop()
    l.pop()


def insert_fn(list):
    for i in range(10_000_000):
        append(list)
        remove(list)
    return True


def size_fn(list):
    for i in range(10_000_000):
        l = len(list)
        assert l % 2 == 0, f"List length was {l}, at attempt {i}"
    return True


shared_list = []
threads = [
    Thread(insert_fn, (shared_list,)),
    Thread(size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
