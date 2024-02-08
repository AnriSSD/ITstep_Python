def group_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same size.")
    grouped_elements = []
    for i in range(len(list1)):
        grouped_elements.append((list1[i], list2[i]))
    return grouped_elements


# ნიმუში
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]

grouped_elements = group_elements(list1, list2)
print(grouped_elements)
