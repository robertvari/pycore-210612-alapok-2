import os


def get_files(root_folder: str, files=[], ext=None) -> list:
    """
    Lists a folder and returns files.
    :param root_folder: str
    :param ext: optional extension filter
    :return: string list of file paths
    """

    assert os.path.exists(root_folder), "Folder does not exist."

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

    files += all_files

    subfolders = [os.path.join(root_folder, i) for i in folder_content if os.path.isdir(os.path.join(root_folder, i))]

    if subfolders:
        for folder in subfolders:
            get_files(folder, files, ext)

    return files
