import threading, time, random

downloading = threading.Event()


def downloader_worker():
    print("Download started")
    time.sleep(random.randint(1, 10))

    print("Download finished")
    downloading.set()


def file_worker():
    downloading.wait()
    print("file_worker started")


t1 = threading.Thread(target=downloader_worker)
t2 = threading.Thread(target=file_worker)

t1.start()
t2.start()

# event commands
# print(downloading.is_set())
# downloading.set()
# print(downloading.is_set())
# downloading.clear()
# print(downloading.is_set())