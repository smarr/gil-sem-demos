from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success

# Check whether there is a correctness issues with concurrent
# append;pop;[] accesses to a list on nogil.


def inc_zero(list):
    for _ in range(1_000_000):
        list[0] += 1


def inc_one_thousand(list):
    for _ in range(1_000_000):
        list[1000] += 1


def append(list):
    for _ in range(1_000_000):
        list.append(1)


def pop(list):
    for _ in range(1_000_000):
        try:
            list.pop()
        except IndexError:
            pass


shared_list = [0] * 1001
threads = [
    Thread(inc_zero, (shared_list,)),
    Thread(inc_one_thousand, (shared_list,)),
    Thread(append, (shared_list,)),
    Thread(pop, (shared_list,)),
]

results = start_and_await(threads)
report_error_or_success(results)
