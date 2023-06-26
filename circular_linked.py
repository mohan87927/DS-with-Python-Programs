import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete_at_front(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        if self.head.next == self.head:
            self.head = None
        else:
            temp.next = self.head.next
            self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        prev.next = self.head

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Menu-driven interface
linked_list = CircularLinkedList()

while True:
    print("\nCircular Linked List Operations:")
    print("1. Append an element")
    print("2. Prepend an element")
    print("3. Delete an element from the front")
    print("4. Delete an element from the end")
    print("5. Display the linked list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to append: "))
        start_time = time.time()
        linked_list.append(data)
        end_time = time.time()
        print("Element appended successfully!")
        print("Time taken:", end_time - start_time, "seconds")

    elif choice == 2:
        data = int(input("Enter the element to prepend: "))
        start_time = time.time()
        linked_list.prepend(data)
        end_time = time.time()
        print("Element prepended successfully!")
        print("Time taken:", end_time - start_time, "seconds")

    elif choice == 3:
        start_time = time.time()
        linked_list.delete_at_front()
        end_time = time.time()
        print("Element deleted from the front successfully!")
        print("Time taken:", end_time - start_time, "seconds")

    elif choice == 4:
        start_time = time.time()
        linked_list.delete_at_end()
        end_time = time.time()
        print("Element deleted from the end successfully!")
        print("Time taken:", end_time - start_time, "seconds")

    elif choice == 5:
        start_time = time.time()
        print("Circular Linked List:")
        linked_list.display()
        end_time = time.time()
        print("Time taken:", end_time - start_time, "seconds")

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
