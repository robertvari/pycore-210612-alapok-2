import threading, time, queue

job_list = queue.Queue()


def process_image_worker():
    while not job_list.empty():
        job = job_list.get()
        print(job)
        time.sleep(1)
        job_list.task_done()


def start_processing(image_list, max_threads=4):
    [
       job_list.put(i) for i in image_list
    ]

    for _ in range(max_threads):
        t = threading.Thread(target=process_image_worker)
        t.start()