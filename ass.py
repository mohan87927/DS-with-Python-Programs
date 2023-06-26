class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
    print("Inserted successfully")
    return root


def preorder_traversal(root):
    if root is not None:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

root = None
while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to insert: "))
        root = insert_node(root, data)

    elif choice == 2:
        print("Pre-order traversal:")
        preorder_traversal(root)

    elif choice == 3:
        print("In-order traversal:")
        inorder_traversal(root)

    elif choice == 4:
        print("Post-order traversal:")
        postorder_traversal(root)

    else:
        print("Enter a valid option")
