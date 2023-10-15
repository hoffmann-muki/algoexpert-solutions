def nodeDepths(tree):
    if tree.left and tree.right:
        return sumDepths(1, tree.left) + sumDepths(1, tree.right)
    elif tree.left and not tree.right:
        return sumDepths(1, tree.left)
    elif tree.right and not tree.left:
        return sumDepths(1, tree.right)
    else:
        return 0

def sumDepths(acc, tree):
    if tree.left and tree.right:
        leftDepths = sumDepths(acc + 1, tree.left)
        rightDepths = sumDepths(acc + 1, tree.right)
        return acc + leftDepths + rightDepths
    elif tree.left and not tree.right:
        return acc + sumDepths(acc + 1, tree.left)
    elif tree.right and not tree.left:
        return acc + sumDepths(acc + 1, tree.right)
    else:
        return acc

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
