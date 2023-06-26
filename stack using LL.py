class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.data

    def traverse(self):
        if self.top is None:
            print("Stack is empty.")
            return

        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Menu-driven interface for stack
stack = Stack()

while True:
    print("\nStack Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the element to push: ")
        stack.push(data)
        print("Element pushed onto the stack.")

    elif choice == 2:
        item = stack.pop()
        if item is not None:
            print("Popped item from the stack:", item)

    elif choice == 3:
        item = stack.peek()
        if item is not None:
            print("Top item of the stack:", item)

    elif choice == 4:
        stack.traverse()

    elif choice == 5:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
