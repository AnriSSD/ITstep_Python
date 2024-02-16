# Node class
class Node:
    def __init__(self, value):
        # Initialize a new node with a given value and a pointer to the next node
        self.value = value
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self, value):
        # Initialize the linked list with a head node
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        # Append a new node with the given value to the end of the list
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self):
        # Remove the last element (tail) from the list
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

# Stack class
class Stack:
    def __init__(self):
        # Initialize an empty stack using a list
        self.stack = []

    def push(self, data):
        # Push an element onto the stack
        self.stack.append(data)

    def pop(self):
        # Pop an element from the stack
        if not self.stack:
            raise IndexError("pop from empty stack")
        return self.stack.pop()

# Example usage of LinkedList
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# Remove the last element
linked_list.remove()
print(linked_list.tail.value) 

# Example usage of Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.pop()) 
print(stack.pop())  
