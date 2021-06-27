import time, random, threading, queue
from utilities.file_utils import get_files

file_list = get_files(r"C:\Work\_PythonSuli\pycore-210612\photos", ext=".jpg")


def worker():
    print("worker started")
    time.sleep(random.randint(1, 10))
    print("worker finished")