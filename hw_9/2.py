from functools import reduce


def multiply_list_elements(numbers):
    try:
        product = reduce(lambda x, y: x * y, numbers)
        return product
    except TypeError:
        return "Input must be a list of numbers."


# მგ
input_list = [1, 2, 3, 4, 5]
output = multiply_list_elements(input_list)
print(output)  # Output: 120
