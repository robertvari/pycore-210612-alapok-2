import time, random, threading


def worker1(worker_name):
    print(f"{worker_name} started")
    time.sleep(random.randint(10, 30))
    print(f"{worker_name} finished")


def worker2(worker_name):
    print(f"{worker_name}  started")
    time.sleep(random.randint(10, 30))
    print(f"{worker_name}  finished")


t1 = threading.Thread(target=worker1, args=["Worker1"])
t2 = threading.Thread(target=worker2, args=["Worker2"])

t1.start()
t2.start()

print("Program finished.")