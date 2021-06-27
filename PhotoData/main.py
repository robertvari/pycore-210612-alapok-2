from utilities.file_utils import get_files, get_root_folder
from utilities.image_utils import start_processing


def main():
    print("-"*50, "WATERMARKER", "-"*50)

    root_folder = get_root_folder()
    photo_files = get_files(root_folder, ext=".jpg")

    start_processing(photo_files)


if __name__ == '__main__':
    main()