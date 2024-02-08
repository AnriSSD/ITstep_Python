total_sum = 0
while True:
    user_input = input("Enter a number (or 'sum' to get the sum): ")
    if user_input == "sum":
        break
    num = int(user_input)
    if num > 0:
        total_sum += num

print(f"The sum of positive numbers entered is: {total_sum}")
