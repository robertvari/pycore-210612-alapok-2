import time, random
from utilities.decorators import my_timer, my_logger


@my_logger
@my_timer
def worker1():
    print("Worker1 started...")
    time.sleep(random.randint(1, 10))
    print("Worker1 finished")

    return 42

worker1()