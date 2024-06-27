# * * * * * * * * * * * Recursive Solution * * * * * * * * * * * * * # 

class BSTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # avg: O(logn) space | O(logn) time
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    # avg: O(logn) space | O(logn) time
    def contains(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left is not None:
                return self.left.contains(value)
        else:
            if self.right is not None:
                return self.right.contains(value)
        return False

    # avg: O(logn) space | O(logn) time
    def remove(self, value):
        pass

# * * * * * * * * * * * Iterative Solution * * * * * * * * * * * * * # 

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # avg: O(1) space | O(logn) time
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # avg: O(1) space | O(logn) time
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

# avg: O(logn) time | O(1) space
    def remove(self, value, parent=None):
        parentNode = parent
        currentNode = self
        if currentNode.isLeafNode():
            return self
        else:
            while currentNode is not None:
                if currentNode.value == value:
                    if currentNode.isLeafNode():
                        if currentNode.value < parentNode.value:
                            parentNode.left = None
                        else:
                            parentNode.right = None
                        break
                    elif parentNode is not None and parentNode.hasOneDescendant():
                        if currentNode.value < parentNode.value:
                            parentNode.value = parentNode.left.value
                            parentNode.left = None
                        else:
                            parentNode.value = parentNode.right.value
                            parentNode.right = None
                        break
                    else:
                        if currentNode.right is not None:
                            currentNode.right.removeSmallestNodeAmongstDescendants(currentNode)
                            if parentNode is None:
                                self = currentNode
                            else:
                                if currentNode.value < parentNode.value:
                                    parentNode.left = currentNode
                                else:
                                    parentNode.right = currentNode
                            break
                        else:
                            if parentNode is None:
                                self = currentNode.left
                            else:
                                if currentNode.value < parentNode.value:
                                    parentNode.left = currentNode.left
                                else:
                                    parentNode.right = currentNode.left
                            break
                elif currentNode.value <= value:
                    parentNode = currentNode
                    currentNode = currentNode.right
                else:
                    parentNode = currentNode
                    currentNode = currentNode.left
        return self
    
    def isLeafNode(self):
        return self is not None and self.left is None and self.right is None
    
    def hasOneDescendant(self):
        return (not self.isLeafNode()) and (self.right is None and self.left is not None and self.left.isLeafNode()) or (self.left is None and self.right is not None and self.right.isLeafNode())
    
    def removeSmallestNodeAmongstDescendants(self, parent):
        parentNode = parent # node to be removed
        currentNode = self # first right node
        while currentNode is not None and currentNode.left is not None:
            parentNode = currentNode
            currentNode = currentNode.left
        parent.value = currentNode.value
        if currentNode.value < parentNode.value:
            parentNode.left = currentNode.right
        else:
            parentNode.right = currentNode.right
