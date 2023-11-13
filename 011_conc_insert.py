from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success

# Check whether a loop with len;list[0] can observe non-atomic behavior
# when another thread is running a loop with append;pop.


def insert_remove_fn(list):
    for _ in range(100_000_000):
        list.append(1)
        list.pop()


def contains_and_size_fn(list):
    for _ in range(100_000_000):
        l = len(list)
        try:
            list[0]
            c = True
        except IndexError:
            c = False
        assert (not c and l == 0) or (
            c and l == 1
        ), f"append;pop not atomic, or not atomically observable. length: {l}, element in list: {c}"


shared_list = []
threads = [
    Thread(insert_remove_fn, (shared_list,)),
    Thread(contains_and_size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
