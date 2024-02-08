def check_even_odd(number):
    if number % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

user_input = int(input("შეიყვანეთ მთელი რიცხვი: "))
check_even_odd(user_input)
