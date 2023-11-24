from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success

# This one is to make sure that we cannot observe the list having a negative length.
# This is an issue with some concurrent data structures on top of other
# language implementations such as the JVM.


def insert_fn(list):
    for _ in range(5_000_000):
        if len(list) == 0:
            list.append(1)


def delete_fn(list):
    for _ in range(5_000_000):
        try:
            list.pop()
        except IndexError:
            pass


def size_fn(list):
    for _ in range(5_000_000):
        l = len(list)
        assert (
            l == 0 or l == 1
        ), f"Unexpected length: {l}. Shouldn't be negative or larger than 1."


shared_list = []
threads = [
    Thread(insert_fn, (shared_list,)),
    Thread(delete_fn, (shared_list,)),
    Thread(size_fn, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
