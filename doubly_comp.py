import time


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
            new_node.prev = temp

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            print("Linked list is empty.")
            return
        if self.head.data == data:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return

        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        if temp is None:
            print(f"{data} is not found in the linked list.")
            return

        if temp.next:
            temp.next.prev = temp.prev
        temp.prev.next = temp.next

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Menu-driven interface
linked_list = DoublyLinkedList()

while True:
    print("\nDoubly Linked List Operations:")
    print("1. Append an element")
    print("2. Prepend an element")
    print("3. Delete an element")
    print("4. Display the linked list")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to append: "))
        start_time = time.time()
        linked_list.append(data)
        end_time = time.time()
        print("Element appended successfully!")
        print("Time taken for the operation:", end_time - start_time, "seconds")

    elif choice == 2:
        data = int(input("Enter the element to prepend: "))
        start_time = time.time()
        linked_list.prepend(data)
        end_time = time.time()
        print("Element prepended successfully!")
        print("Time taken for the operation:", end_time - start_time, "seconds")

    elif choice == 3:
        data = int(input("Enter the element to delete: "))
        start_time = time.time()
        linked_list.delete(data)
        end_time = time.time()
        print("Element deleted successfully!")
        print("Time taken for the operation:", end_time - start_time, "seconds")

    elif choice == 4:
        print("Linked list:")
        linked_list.display()

    elif choice == 5:
        break

    else:
        print("Invalid choice. Please try again.")
