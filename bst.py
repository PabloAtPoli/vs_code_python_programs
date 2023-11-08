# Python program to insert a node
# in a BST

# Given Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
# Function to insert a new node with
# given key in BST


def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    # Return the node pointer
    return node

# Function to do inorder traversal of BST


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


def preorder(root):
    if root is not None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

 # Returns height of the BST


def height(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        left_depth = height(node.left)
        right_depth = height(node.right)

        # Use the larger one
        if left_depth > right_depth:
            return (left_depth + 1)
        else:
            return (right_depth + 1)

# Print nodes at a given level


def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.key, end=" ")
    elif level > 1:
        # Recursive call
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)

# Function to line by line print
# level order traversal of a tree


def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)
        print()

# Function to print leaf nodes
# from left to right


def print_leaf_nodes(root):
    # If node is null, return
    if not root:
        return

    # If node is leaf node,
    # print its data
    if not root.left and not root.right:
        print(root.key, end=" ")

    # If left child exists,
    # check for leaf recursively
    if root.left:
        print_leaf_nodes(root.left)

    # If right child exists,
    # check for leaf recursively
    if root.right:
        print_leaf_nodes(root.right)


def print_non_leaf_node(root):
    # Base Cases
    if root is None or (root.left is None and root.right is None):
        return

    # If current node is non-leaf,
    if root.left is not None or root.right is not None:
        print(root.key, end=" ")

    # If root is Not NULL and one
    # of its children is also not NULL
    print_non_leaf_node(root.left)
    print_non_leaf_node(root.right)


# Driver Code
if __name__ == '__main__':
    """ 
    Let us create following BST 
       50 
      /	 \ 
    30	 70 
    / \ / \  
20 40 60 80 
/
10   
    """
    root = None

    # Inserting value 50
    root = insert(root, 50)

    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    insert(root, 10)

    # Print the BST
    print("Inorder Traversal:", end=" ")
    inorder(root)
    print()

    print("Preorder Traversal:", end=" ")
    preorder(root)
    print()

    print("Postorder Traversal:", end=" ")
    postorder(root)
    print()

    print(f"The height of the binary tree is {height(root)}")

    print("The nodes of level 3 are the following:")
    print_given_level(root, 3)
    print()

    print("The nodes of level 2 are the following:")
    print_given_level(root, 2)
    print()

    print("The binary tree by levels is the following:")
    print_level_order(root)
    print()

    print("The leaf nodes are the following:")
    print_leaf_nodes(root)
    print()

    print("The nodes that are not leaft are the following:")
    print_non_leaf_node(root)
