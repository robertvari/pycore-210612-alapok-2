import os


def get_files(root_folder: str, ext=None) -> list:
    """
    Lists a folder and returns files.
    :param root_folder: str
    :param ext: optional extension filter
    :return: string list of file paths
    """

    # collect all content (files/folders)
    folder_content = os.listdir(root_folder)

    # collect all filer
    all_files = [
        os.path.join(root_folder, i) for i in folder_content
        if os.path.isfile(os.path.join(root_folder, i))
    ]

    # if we are using extension filter
    if ext:
        all_files = [
            i for i in all_files
            if os.path.splitext(i)[1].lower() == ext.lower()
        ]

    assert os.path.exists(root_folder), "Folder does not exist."

    return []


if __name__ == '__main__':
    #folder_path = r"C:\Work\_PythonSuli\pycore-210612\photos"
    # result = get_files(folder_path)
    print(os.path.splitext(r"C:\Work\_PythonSuli\pycore-210612\photos\IMG_1069.JPG"))