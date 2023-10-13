from threading import Thread


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
        assert (not c and l == 0) or (c and l == 1)


shared_list = []
threads = [
    Thread(target=insert_remove_fn, args=(shared_list,)),
    Thread(target=contains_and_size_fn, args=(shared_list,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Done")
