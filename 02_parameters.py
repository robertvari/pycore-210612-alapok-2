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


# random length params
def rand_number_of_arguments(*args):
    for i in args:
        print(i)


# random length keyword params
def rand_number_of_keyword_args(**kwargs):
    print(kwargs)

rand_number_of_keyword_args(
    name="Robert",
    age=42,
    email="robert@gmail.com"
)