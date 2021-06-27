from utilities.file_utils import get_files

photo_folder = r"C:\Work\_PythonSuli\pycore-210612\photos"


def call_myself(i):
    if i >= 10:
        print("i >= 10. exit.")
    else:
        print(f"I called myself {i} times.")
        call_myself(i+1)