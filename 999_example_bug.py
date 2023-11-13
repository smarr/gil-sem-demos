from gil_sem import ResultThread as Thread, start_and_await, report_error_or_success


class Example(object):
    def __init__(self):
        self.id = 0
        self.usage = [0] * 1_000

    def get_id(self):
        # expected to be atomic: start
        request_id = self.id
        self.id += 1
        # expected to be atomic: end

        self.usage[request_id % 1_000] += 1

        return request_id


obj = Example()


def loop_get_id():
    for _ in range(10_000_000):
        obj.get_id()


threads = [
    Thread(loop_get_id, ()),
    Thread(loop_get_id, ()),
]

results = start_and_await(threads)

for usage_cnt in obj.usage:
    assert (
        usage_cnt == 20_000
    ), f"+= not atomic. If atomic, ids are used 2000 times, but one was used {usage_cnt} times."
print("Completed")
