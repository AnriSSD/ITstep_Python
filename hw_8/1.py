int_list = [10, 20, 30, 40]


def add_to_list(num):
    global int_list
    int_list.append(num)


# Nimushi

add_to_list(50)
print(int_list)
