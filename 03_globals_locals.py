# global scope
name = "Robert"


def print_name():
    # local scope
    # name = "Tamás"
    print(name)


def change_global_name():
    global name
    name = "Kriszta"

change_global_name()
print_name()
print(name)