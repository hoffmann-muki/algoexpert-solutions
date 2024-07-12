# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isSymmetrical=True):
        self.isSymmetrical = isSymmetrical

# O(n) time | O(h) space
def symmetricalTree(tree):
    treeInfo = TreeInfo()
    compareNodesForSymmetry(tree.left, tree.right, treeInfo)
    return treeInfo.isSymmetrical

def compareNodesForSymmetry(tree1, tree2, treeInfo):
    if tree1 is None and tree2 is None:
        return
    elif tree1 is None and tree2 is not None:
        treeInfo.isSymmetrical = False
        return
    elif tree1 is not None and tree2 is None:
        treeInfo.isSymmetrical = False
        return
    else:
        if tree1.value != tree2.value:
            treeInfo.isSymmetrical = False
            return
        compareNodesForSymmetry(tree1.left, tree2.right, treeInfo)
        compareNodesForSymmetry(tree1.right, tree2.left, treeInfo)
