import time, random, threading, queue
from utilities.file_utils import get_files

job_list = queue.Queue()
[
    job_list.put(i) for i in get_files(r"C:\Work\_PythonSuli\pycore-210612\photos", ext=".jpg")
]


def worker():
    while not job_list.empty():
        next_file = job_list.get()

        print(f"Working on: {next_file}")
        time.sleep(random.randint(1, 10))
        print("Worker finished")

        job_list.task_done()