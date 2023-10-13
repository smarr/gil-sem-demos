from threading import Thread
from time import perf_counter_ns


def thread_fn(thread_id):
    i = 0
    for _ in range(100_000_000):
        i += 1


threads = [Thread(target=thread_fn, args=(thread_id,)) for thread_id in range(10)]

start_time = perf_counter_ns()
for t in threads:
    t.start()
for t in threads:
    t.join()

end_time = perf_counter_ns()

print(f"Time taken: {(end_time - start_time) // 1_000_000} ms")
