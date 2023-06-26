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
linked_list = LinkedList()

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
