my_list = [43, '22', 12, 66, 210, ["hi"]]

# a. Print the index of 210
print("Index of 210:", my_list.index(210))

# b. Add the text "hello" to the last element
my_list[-1].append("hello")

# c. Delete the element at the second index and print the list
del my_list[2]
print("Modified list:", my_list)

# d. Create a new list my_list_2 with the value of my_list, clear my_list_2, and print both lists
my_list_2 = my_list.copy()
my_list_2.clear()
print("my_list:", my_list)
print("my_list_2:", my_list_2)
