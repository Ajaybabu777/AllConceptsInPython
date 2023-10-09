class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    print(left_height)
    right_height = height(node.right)
    print(right_height)
    sum = 1 + max(left_height, right_height)
    return sum

def diameter(root):
	if root is None:
		return 0
	lheight = height(root.left)
	print(lheight)
	rheight = height(root.right)
	print(rheight)
	ldiameter = diameter(root.left)
	print(ldiameter)
	rdiameter = diameter(root.right)
	print(ldiameter)

	return max(lheight + rheight + 1, max(ldiameter, rdiameter))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("diamter = ",diameter(root))