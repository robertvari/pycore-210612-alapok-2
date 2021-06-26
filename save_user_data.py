def main():
    # get data from user
    user_data = get_user_data()

    # save data to a text file
    save_data(user_data)


def get_user_data():
    """
    Gets data from user.
    :return: str
    """

    name = input("Name:")
    age = input("Age:")
    email = input("Email:")

    return f"Name:{name}\nAge:{age}\nEmail:{email}"


def save_data(user_data):
    """
    Saves user data into a .txt file
    :param user_data: str
    :return: None
    """

    with open("user_data.txt", "w") as f:
        f.write(user_data)

    print("Data saved!")


main()
