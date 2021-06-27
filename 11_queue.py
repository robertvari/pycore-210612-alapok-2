import time, random, threading, queue
from utilities.file_utils import get_files

MAX_THREADS = 8


job_list = queue.Queue()
[
    job_list.put(i) for i in get_files(r"C:\Work\_PythonSuli\pycore-210612\photos", ext=".jpg")
]


def worker():
    worker_name = f"Worker-{threading.currentThread().name}"
    while not job_list.empty():
        next_file = job_list.get()

        print(f"{worker_name} working on: {next_file}")
        time.sleep(random.randint(1, 10))
        print(f"{worker_name} worker finished")

        job_list.task_done()


for _ in range(MAX_THREADS):
    t = threading.Thread(target=worker)
    t.start()