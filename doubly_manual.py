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

    def delete_at_front(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        temp = self.head
        if temp.next is None:
            self.head = None
            return
        while temp.next:
            temp = temp.next
        temp.prev.next = None

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
    print("3. Delete at front")
    print("4. Delete at end")
    print("5. Display the linked list")
    print("6. Exit")

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
        start_time = time.time()
        linked_list.delete_at_front()
        end_time = time.time()
        print("Deleted at front successfully!")
        print("Time taken for the operation:", end_time - start_time, "seconds")

    elif choice == 4:
        start_time = time.time()
        linked_list.delete_at_end()
        end_time = time.time()
        print("Deleted at end successfully!")
        print("Time taken for the operation:", end_time - start_time, "seconds")

    elif choice == 5:
        print("Linked list:")
        linked_list.display()

    elif choice == 6:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
