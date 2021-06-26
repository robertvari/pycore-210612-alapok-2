def main():
    # get data from user
    user_data = get_user_data()

    # save data to a text file
    save_data(user_data)


def get_user_data():
    name = input("Name:")
    age = input("Age:")
    email = input("Email:")

    return f"Name:{name}\nAge:{age}\nEmail:{email}"


def save_data(user_data):
    with open("user_data.txt", "w") as f:
        f.write(user_data)

    print("Data saved!")


main()
