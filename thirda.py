# Stack using Array - Library Book Management

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, book):
        self.stack.append(book)
        print(f'"{book}" added to the stack.')

    # Pop operation
    def pop(self):
        if self.is_empty():
            print("Stack is empty. No book to remove.")
        else:
            book = self.stack.pop()
            print(f'"{book}" removed from the stack.')

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("\nBooks in Stack (Top to Bottom):")
            for book in reversed(self.stack):
                print(book)

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0


# Main Program
library = Stack()

while True:
    print("\n--- Library Book Stack Menu ---")
    print("1. Push (Add Book)")
    print("2. Pop (Remove Book)")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book title: ")
        library.push(book)

    elif choice == 2:
        library.pop()

    elif choice == 3:
        library.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")
