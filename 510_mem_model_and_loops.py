from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success
from time import sleep

# Check whether the Python memory model allows to optimize field reads out of loops.


class FlagObj:
    def __init__(self):
        self.keep_looping = True


obj = FlagObj()


def loop_fn(obj):
    while obj.keep_looping:
        pass


def wait_fn(obj):
    sleep(5)
    obj.keep_looping = False


threads = [
    Thread(loop_fn, (obj,)),
    Thread(wait_fn, (obj,)),
]

results = start_and_await(threads, 10)
report_error_or_success(results)
