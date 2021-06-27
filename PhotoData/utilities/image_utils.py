import threading, time, queue, os
from PIL import Image

job_list = queue.Queue()
thumb_size = 128


def process_image_worker():
    while not job_list.empty():
        image_path = job_list.get()
        print(f"Resizing image: {image_path}")

        image_folder = os.path.dirname(image_path)
        thumbnail_dir = os.path.join(image_folder, "_thumbnails")
        if not os.path.exists(thumbnail_dir):
            os.makedirs(thumbnail_dir)

        # open image
        img = Image.open(image_path)

        # resize image
        img.thumbnail((thumb_size, thumb_size))

        # save thumbnail
        img.save(os.path.join(thumbnail_dir, os.path.basename(image_path)))

        job_list.task_done()


def start_processing(image_list, max_threads=1):
    [
       job_list.put(i) for i in image_list
    ]

    for _ in range(max_threads):
        t = threading.Thread(target=process_image_worker)
        t.start()