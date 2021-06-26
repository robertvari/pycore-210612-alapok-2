name = "Robert"

def main():
    print("main called", name)

    def nested_function():
        print("nested_function called", name)

    nested_function()

