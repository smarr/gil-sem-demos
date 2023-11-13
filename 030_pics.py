from threading import Barrier
from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success

# This one is to test the lookup cache semantics.
# This is more of a theoretical nature, and thus, not likely to show any issues.
# The current implementations should not fail on this test.


class A:
    def get_int(self):
        return 1


class B:
    def get_int(self):
        return 2


def thread_fn(expected_int, obj, barrier):
    for _ in range(10_000):
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()

        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()

        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        assert expected_int == obj.get_int()
        barrier.wait()


shared_list = []
b = Barrier(2)
threads = [
    Thread(thread_fn, (1, A(), b)),
    Thread(thread_fn, (2, B(), b)),
]

results = start_and_await(threads)
report_error_or_success(results)
