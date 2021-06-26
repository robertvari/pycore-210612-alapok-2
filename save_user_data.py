def main():
    print("main called")

    # get data from user
    user_data = get_user_data()

    # save data to a text file
    save_data(user_data)


def get_user_data():
    print("get_user_data called")

    return "Robert\n42\nrobert@gmail.com"


def save_data(user_data):
    print("save_data called", user_data)


main()
