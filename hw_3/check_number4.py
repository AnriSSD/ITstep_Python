num_list = [44, 23, 11, 8, 20, 56, 33, 55]

def check_number_condition(number):
    if number > num_list[2] and number < num_list[-1]:
        print("More than list elements")
    elif number == num_list[5]:
        print("Equal")
    else:
        print("Noneწ of the conditions were met")

user_input = int(input("Enter a number: "))
check_number_condition(user_input)
