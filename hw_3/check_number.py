num_list = [44, 23, 11, 8, 20, 56, 33, 55]

def check_number_in_list(number):
    if number in num_list:
        print("The number is in the list")
    else:
        print("The number is not in the list")

user_input = int(input("Enter a number: "))
check_number_in_list(user_input)