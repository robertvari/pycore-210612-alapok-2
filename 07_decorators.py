import time, random
from utilities.decorators import my_timer


@my_timer
def worker1(name):
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 finished")

    return 42

result = worker1("Robert")