class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        dequeued_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_item

    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None
        return self.front.data

    def traverse(self):
        if self.front is None:
            print("Queue is empty.")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Menu-driven interface for queue
queue = Queue()

while True:
    print("\nQueue Operations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Traverse")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = input("Enter the element to enqueue: ")
        queue.enqueue(data)
        print("Element enqueued into the queue.")

    elif choice == 2:
        item = queue.dequeue()
        if item is not None:
            print("Dequeued item from the queue:", item)

    elif choice == 3:
        item = queue.peek()
        if item is not None:
            print("Front item of the queue:", item)

    elif choice == 4:
        queue.traverse()

    elif choice == 5:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
