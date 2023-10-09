class Node:
    def __init__(self,item):
        self.item = item
        self.right = None
        self.left = None

def preorder(root):
    if root is not None:
        print(root.item)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.item)
        inorder(root.right)



def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.item)


    # def postorder(root):

rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(5)
rootNode.left.right = Node(4)
rootNode.right.right = Node(8)

# preorder(rootNode)
postorder(rootNode)



