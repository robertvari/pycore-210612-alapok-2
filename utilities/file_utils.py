import os


def get_files(root_folder: str, ext=".jpg") -> list:
    """
    Lists a folder and returns .jpg images
    :param root_folder: str
    :return: string list of file paths
    """
    assert os.path.exists(root_folder), "Folder does not exist."

    files = [i for i in os.listdir(root_folder) if os.path.splitext(i)[1].lower() == ext.lower()]

    return files


if __name__ == '__main__':
    folder_path = r"C:\Work\_PythonSuli\pycore-210612\photos"
    result = get_files(folder_path, ext=".XLSX")
    print(result)