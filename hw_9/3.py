def odd_numbers(num_list):
    if not isinstance(num_list, list) or not all(
        isinstance(x, (int, float)) for x in num_list
    ):
        raise TypeError("Input must be a list of numbers.")
    return [x for x in num_list if x % 2 != 0]


# ნიმუში
num_list = [1, 2, 3, 4, 5, 6, 7]

odd_numbers = odd_numbers(num_list)
print(odd_numbers)
