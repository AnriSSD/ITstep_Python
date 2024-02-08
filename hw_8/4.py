def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + recursive_sum(num // 10)


def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + recursive_sum(num // 10)


print(recursive_sum(12345))
