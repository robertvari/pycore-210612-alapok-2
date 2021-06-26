def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a*b


def subdivide_numbers(a, b):
    return a/b


def print_result(result):
    print(f"The result is: {result}")


result = add_numbers(2, 2)
result = multiply_numbers(result, 10)
result = subdivide_numbers(result, 2)

print_result(result)