my_list = []

while True:
    command = input("Enter command (a - append, r - remove, e - exit): ")
    
    if command == 'a':
        number = int(input("Enter number to append: "))
        my_list.append(number)
    elif command == 'r':
        number = int(input("Enter number to remove: "))
        if number in my_list:
            my_list.remove(number)
        else:
            print(f"{number} not found in the list.")
    elif command == 'e':
        break
    else:
        print("Invalid command. Please enter 'a', 'r', or 'e'.")

print("Final list:", my_list)
