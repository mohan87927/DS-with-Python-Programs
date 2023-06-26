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

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not found.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node

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


# Example usage:
linked_list = DoublyLinkedList()

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
