def reverse_string(str):
    if len(str) == 0:
        return ""
    else:
        return str[-1] + reverse_string(str[:-1])


print(reverse_string("Gamarjoba"))
