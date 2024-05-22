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


# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

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

# Function that returns the node with minimum
# key value found in that tree
def min_value_node(node):
    current = node
 
    # Loop down to find the leftmost leaf
    while current and current.left is not None:
        current = current.left
 
    return current

# Function that deletes the key and
# returns the new root
def delete_node(root, key):
    # base Case
    if root is None:
        return root
 
    # If the key to be deleted is smaller than the root's key,
    # then it lies in left subtree
    if key < root.key:
        root.left = delete_node(root.left, key)
 
    # If the key to be deleted is greater than the root's key,
    # then it lies in right subtree
    elif key > root.key:
        root.right = delete_node(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children: Get the inorder successor(smallest
        # in the right subtree)
        temp = min_value_node(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = delete_node(root.right, temp.key)
 
    return root

# Driver Code
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

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

print("Search of 70 in tree:",search(root, 70).key)
    
result = search(root, 100)
if result is not None:
     print("Search of 100 in tree:", result.key)
else:
    print("100 is not in the tree")

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

# print("The nodes of level 3 are the following:")
# print_given_level(root, 3)
# print()

# print("The nodes of level 2 are the following:")
# print_given_level(root, 2)
# print()

# print("The binary tree by levels is the following:")
# print_level_order(root)
# print()

# print("The leaf nodes are the following:")
# print_leaf_nodes(root)
# print()

# print("The nodes that are not leaft are the following:")
# print_non_leaf_node(root)

print("\nDelete 50")
root = delete_node(root, 50)
print("Inorder Traversal after deletion of 50:", end=" ")
inorder(root)

print("\nDelete 10")
root = delete_node(root, 10)
print("Inorder Traversal after deletion of 10:", end=" ")
inorder(root)



