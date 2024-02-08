# 1
def utf8_encode(s):
    return s.encode("utf-8")


# Example
print(utf8_encode("Hello, world!"))


# 2
def process_string(s):
    s = s.strip()
    s = s.lower()
    s = s.replace("python", "Python")
    return s + "Python"


# Example
print(process_string("   Python is FUNNY   "))

# 3


def first_half(s):
    return s[: len(s) // 2]


# Example
print(first_half("Python is cool"))


# 4
import string


def is_valid(s):
    return len(s) == 1 and s.isdigit()


# Example
print(is_valid("5"))
print(is_valid("A"))


# 5
def convert_string_to_bytes_and_back(s):
    bytes_value = s.encode("utf-8")
    print("Bytes:", bytes_value)
    string_value = bytes_value.decode("utf-8")
    print("String:", string_value)


# Example
convert_string_to_bytes_and_back("Hello, world!")
