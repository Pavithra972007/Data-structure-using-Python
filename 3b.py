# Node class
class Node:
    def __init__(self, title):
        self.title = title
        self.next = None

# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, title):
        new_node = Node(title)
        new_node.next = self.top
        self.top = new_node
        print(f'"{title}" added to the stack.')

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty. No book to retrieve.")
            return None

        removed_book = self.top.title
        self.top = self.top.next
        print(f'"{removed_book}" retrieved from the stack.')
        return removed_book

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty.")
            return

        print("\nBooks in the stack (Top to Bottom):")
        current = self.top
        while current:
            print(current.title)
            current = current.next

# Main Program
stack = Stack()

while True:
    print("\nLibrary Stack Operations")
    print("1. Push (Add Book)")
    print("2. Pop (Retrieve Book)")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book title: ")
        stack.push(book)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
