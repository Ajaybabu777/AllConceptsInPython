class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def isBalanced(root):
    def checkHeight(node):
        if not node:
            return 0

        left_height = checkHeight(node.left)
        if left_height == -1:
            return -1

        right_height = checkHeight(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    # return checkHeight(root) != -1
    if root.val !=-1:
        return checkHeight(root) != None

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)

if isBalanced(root) == True:
    print("tree is balanced")
else:
    print("tree is unbalamced")
