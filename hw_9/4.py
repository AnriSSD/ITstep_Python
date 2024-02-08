def filter_strings_ending_with(string_list, ending):
    if not isinstance(string_list, list) or not all(
        isinstance(x, str) for x in string_list
    ):
        raise TypeError("Input must be a list of strings.")
    return [x for x in string_list if x.endswith(ending)]


# ნიმუში
string_list = ["hello", "world", "coding", "nod"]
ending = "ing"

filtered_strings = filter_strings_ending_with(string_list, ending)
print(filtered_strings)
