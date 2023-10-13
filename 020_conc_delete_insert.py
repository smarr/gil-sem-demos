from threading import Thread


def insert_fn(list):
    for _ in range(100_000_000):
        if len(list) == 0:
            list.append(1)


def delete_fn(list):
    for _ in range(100_000_000):
        try:
            list.pop()
        except IndexError:
            pass


def size_fn(list):
    for _ in range(100_000_000):
        l = len(list)
        assert l == 0 or l == 1, l


shared_list = []
threads = [
    Thread(target=insert_fn, args=(shared_list,)),
    Thread(target=delete_fn, args=(shared_list,)),
    Thread(target=size_fn, args=(shared_list,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Done")
