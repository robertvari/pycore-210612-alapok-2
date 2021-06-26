import time, random


def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 finished")

def worker2():
    print("Worker2 started...")
    time.sleep(random.randint(1, 10))
    print("Worker2 finished")

def worker3():
    print("Worker3 started...")
    time.sleep(random.randint(1, 10))
    print("Worker3 finished")


start = time.time()
worker1()
print(f"Process time: {time.time() - start}")
