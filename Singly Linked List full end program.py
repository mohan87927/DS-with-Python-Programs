class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not found.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, data):
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            print(f"{data} is not found in the linked list.")
            return

        prev.next = temp.next

    def search(self, data):
        if self.head is None:
            print("Linked list is empty.")
            return False

        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next

        return False

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


LL = LinkedList()

while True:
    print("\nLinked List Operations:")
    print("1. Append")
    print("2. Prepend")
    print("3. Insert After")
    print("4. Delete")
    print("5. Search")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to append: "))
        LL.append(data)
        print("Element appended successfully!")

    elif choice == 2:
        data = int(input("Enter the element to prepend: "))
        LL.prepend(data)
        print("Element prepended successfully!")

    elif choice == 3:
        data = int(input("Enter the element to insert: "))
        prev_data = int(input("Enter the element after which to insert: "))
        prev_node = None
        temp = LL.head
        while temp:
            if temp.data == prev_data:
                prev_node = temp
                break
            temp = temp.next
        LL.insert_after(prev_node, data)
        print("Element inserted successfully!")

    elif choice == 4:
        data = int(input("Enter the element to delete: "))
        LL.delete(data)
        print("Element deleted successfully!")

    elif choice == 5:
        data = int(input("Enter the element to search: "))
        if LL.search(data):
            print(f"{data} is found in the linked list.")
        else:
            print(f"{data} is not found in the linked list.")

    elif choice == 6:
        print("Linked List:")
        LL.display()

    elif choice == 7:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
