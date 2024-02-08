import re

def validate_phone_number(phone_number):
    pattern = r"\(\d{3}\) \d{3}-\d{3}"
    if re.match(pattern, phone_number):
        return phone_number
    else:
        return "Invalid format"

# Example
phone_number = input("Enter a phone number (in the format (123) 456-789): ")
result = validate_phone_number(phone_number)
print(result)
