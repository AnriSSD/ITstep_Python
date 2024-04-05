import threading


# Function to find even numbers in the range
def find_evens():
    for number in range(30, 51):
        if number % 2 == 0:
            print(f"Even number: {number}")


# Function to find odd numbers in the range
def find_odds():
    for number in range(30, 51):
        if number % 2 != 0:
            print(f"Odd number: {number}")


# Creating threads for each function
even_thread = threading.Thread(target=find_evens)
odd_thread = threading.Thread(target=find_odds)

# Starting the threads
even_thread.start()
odd_thread.start()

# Waiting for both threads to complete
even_thread.join()
odd_thread.join()
