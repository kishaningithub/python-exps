from time import sleep

def expensive_compute():
    for x in range(10):
        sleep(1)
        yield x

for x in expensive_compute():
    print(x)