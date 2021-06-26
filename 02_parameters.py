# required positional param.
def say_hello(name):
    print(f"Hello {name}!")


# multiple required positional param
def user_data(name: str, age: int, email: str):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")