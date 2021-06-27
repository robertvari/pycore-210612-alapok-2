add_number = lambda a, b: a + b
multiply_numbers = lambda a, b: a * b
divide_numbers = lambda a, b: a / b

print_my_name = lambda name: name.upper()

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna"]

print(sorted(name_list))
print(sorted(name_list, key=lambda name: name.split()[-1]))
