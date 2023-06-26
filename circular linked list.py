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

    def insert_after(self, prev_node, data):
        if not prev_node:
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
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            if self.head.next == self.head:
                self.head = None
            else:
                temp.next = self.head.next
                self.head = self.head.next
            return

        temp = self.head
        prev = None
        while temp.next != self.head:
            prev = temp
            temp = temp.next
            if temp.data == data:
                prev.next = temp.next
                return

        print(f"{data} is not found in the linked list.")

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


# Example usage:
linked_list = CircularLinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display()  # Output: 1 2 3

linked_list.prepend(0)

linked_list.display()  # Output: 0 1 2 3

linked_list.insert_after(linked_list.head.next, 1.5)

linked_list.display()  # Output: 0 1 1.5 2 3

linked_list.delete(1.5)

linked_list.display()  # Output: 0 1 2 3
