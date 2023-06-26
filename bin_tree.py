# Binary Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node into the binary tree
def insert_node(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert_node(root.left, data)
        else:
            root.right = insert_node(root.right, data)
    return root

# In-order traversal (Left, Root, Right)
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

# Pre-order traversal (Root, Left, Right)
def preorder_traversal(root):
    if root is not None:
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Post-order traversal (Left, Right, Root)
def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

# Create an empty binary tree
root = None

# Menu-driven interface
while True:
    print("\nBinary Tree Operations:")
    print("1. Insert an element")
    print("2. In-order traversal")
    print("3. Pre-order traversal")
    print("4. Post-order traversal")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to insert: "))
        root = insert_node(root, data)
        print("Element inserted successfully!")

    elif choice == 2:
        print("In-order traversal:")
        inorder_traversal(root)

    elif choice == 3:
        print("Pre-order traversal:")
        preorder_traversal(root)

    elif choice == 4:
        print("Post-order traversal:")
        postorder_traversal(root)

    elif choice == 5:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")
