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
		print(root.key,end=" ")
		
def preorder(root):
	if root is not None:
		print(root.key,end=" ")
		preorder(root.left)
		preorder(root.right)




# Driver Code 
if __name__ == '__main__': 
	""" 
	Let us create following BST 
		50 
	/	 \ 
	30	 70 
	/ \ / \ 
	20 40 60 80 
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
	
#This code is contributed by japmeet01
