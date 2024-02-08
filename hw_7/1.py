def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n + 1):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


# ნიმუში
n = 10
fibonacci_numbers = fibonacci_sequence(n)
print(fibonacci_numbers)
