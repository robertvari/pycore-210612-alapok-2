# required positional param.
def say_hello(name):
    print(f"Hello {name}!")


# multiple required positional param
def user_data(name: str, age: int, email: str):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")


# default parameters
def user_data2(name, age=10, email="peter@gmail.com"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")

user_data2("Robert", 42, "robert@gmail.com")

# keyword arguments
user_data2(
    email="robert@gmail.com",
    name="Robert",
    age=42
)