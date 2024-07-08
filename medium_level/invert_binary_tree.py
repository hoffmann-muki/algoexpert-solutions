# O(n) time | O(logn) space
def invertBinaryTree(tree):
    if tree.left is None and tree.right is None:
        return
    elif tree.left is not None and tree.right is None:
        tree.right = tree.left
        tree.left = None
        invertBinaryTree(tree.right)
    elif tree.left is None and tree.right is not None:
        tree.left = tree.right
        tree.right = None
        invertBinaryTree(tree.left)
    else:
        tempNode = tree.right
        tree.right = tree.left
        tree.left = tempNode
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)

# O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
