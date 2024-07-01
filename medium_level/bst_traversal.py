# left -> middle -> right
def inOrderTraverse(tree, array):
    if tree.left is not None and tree.right is not None:
        return inOrderTraverse(tree.left, []) + [tree.value] + inOrderTraverse(tree.right, [])
    elif tree.left is not None and tree.right is None:
        return inOrderTraverse(tree.left, []) + [tree.value]
    elif tree.left is None and tree.right is not None:
        return [tree.value] + inOrderTraverse(tree.right, [])
    else:
        return [tree.value]

# middle -> left -> right
def preOrderTraverse(tree, array):
    if tree.left is not None and tree.right is not None:
        return [tree.value] + preOrderTraverse(tree.left, []) + preOrderTraverse(tree.right, [])
    elif tree.left is not None and tree.right is None:
        return [tree.value] + preOrderTraverse(tree.left, [])
    elif tree.left is None and tree.right is not None:
        return [tree.value] + preOrderTraverse(tree.right, [])
    else:
        return [tree.value]

# left -> right -> middle
def postOrderTraverse(tree, array):
    if tree.left is not None and tree.right is not None:
        return postOrderTraverse(tree.left, []) + postOrderTraverse(tree.right, []) + [tree.value]
    elif tree.left is not None and tree.right is None:
        return postOrderTraverse(tree.left, []) + [tree.value]
    elif tree.left is None and tree.right is not None:
        return postOrderTraverse(tree.right, []) + [tree.value]
    else:
        return [tree.value]
