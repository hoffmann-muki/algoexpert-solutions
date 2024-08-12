# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def bindNodes(self, nodeOne, nodeTwo):
        nodeOne.next = nodeTwo
        nodeTwo.prev = nodeOne
    
    def setHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        if self.head.value == node.value:
            return
        current = self.head.next
        previous = self.head
        while current != None:
            if current.value == node.value:
                if current.next is None: # remove current
                    previous.next = None
                    self.tail = previous
                else:
                    self.bindNodes(previous, current.next)
                break
            current = current.next
            previous = previous.next
        self.bindNodes(node, self.head)
        self.head = node
        
    def setTail(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return
        if self.tail.value == node.value:
            return
        current = self.tail.prev
        previous = self.tail
        while current != None:
            if current.value == node.value:
                if current.prev is None: # remove current
                    previous.prev = None
                    self.head = previous
                else:
                    self.bindNodes(current.prev, previous)
                break
            current = current.prev
            previous = previous.prev
        self.bindNodes(self.tail, node)
        self.tail = node
    
    def insertBefore(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        current = self.head
        previous = None
        while current != None:
            if current.value == node.value:
                if previous == None:
                    self.bindNodes(nodeToInsert, current)
                    self.head = nodeToInsert
                else:
                    self.bindNodes(previous, nodeToInsert)
                    self.bindNodes(nodeToInsert, current)
                break
            current = current.next
            previous = current.prev if current else current
    
    def insertAfter(self, node, nodeToInsert):
        self.remove(nodeToInsert)
        current = self.head
        previous = None
        while current != None:
            if current.value == node.value:
                if current.next == None:
                    self.bindNodes(current, nodeToInsert)
                    self.tail = nodeToInsert
                else:
                    self.bindNodes(nodeToInsert, current.next)
                    self.bindNodes(current, nodeToInsert)
                break
            current = current.next
            previous = current.prev if current else current

    def insertAtPosition(self, position, nodeToInsert):
        currentPosition = 1
        current = self.head
        previous = None
        while current != None:
            if currentPosition == position:
                if current.value == nodeToInsert.value:
                    return
                else:
                    self.remove(Node(nodeToInsert.value))
                    self.insertNodeAtPosition(position, nodeToInsert)
                break
            currentPosition += 1
            current = current.next
            previous = current.prev if current else current

    def insertNodeAtPosition(self, position, nodeToInsert):
        currentPosition = 1
        current = self.head
        previous = None
        while current != None:
            if currentPosition == position:
                if previous == None:
                    self.bindNodes(nodeToInsert, current)
                    self.head = nodeToInsert
                else:
                    self.bindNodes(nodeToInsert, current)
                    self.bindNodes(previous, nodeToInsert)
                break
            currentPosition += 1
            current = current.next
            previous = current.prev if current else current
    
    def removeNodesWithValue(self, value):
        current = self.head
        previous = None
        while current != None:
            if current.value == value:
                if previous == None: # removing the head
                    if current.next == None:
                        self.head = None
                        self.tail = None
                    else:
                        current.next.prev = None
                        self.head = current.next
                else:
                    if current.next == None:
                        previous.next = None
                        self.tail = previous
                    else:
                        self.bindNodes(previous, current.next)
            current = current.next
            previous = current.prev if current else current

    def remove(self, node):
        if not self.head: # empty list
            return
        current = self.head
        previous = None
        while current != None:
            if current.value == node.value:
                if previous == None: # removing the head
                    if current.next == None:
                        self.head = None
                        self.tail = None
                    else:
                        current.next.prev = None
                        self.head = current.next
                else:
                    if current.next == None:
                        previous.next = None
                        self.tail = previous
                    else:
                        self.bindNodes(previous, current.next)
                break
            current = current.next
            previous = current.prev if current else current

    def containsNodeWithValue(self, value):
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False

# ---------------------------- Testing --------------------------- #

linkedList = DoublyLinkedList()
one = Node(1)
two = Node(2)
linkedList.bindNodes(one, two)
linkedList.head = one
linkedList.tail = two

def iterateThroughListForwards(list):
    print('forwards')
    current = list.head
    while current != None:
        print((current.prev.value if current.prev else None, current.value, current.next.value if current.next else None), end=' ')
        current = current.next
    print()

def iterateThroughListBackwards(list):
    print('backwards')
    current = list.tail
    while current != None:
        print((current.prev.value if current.prev else None, current.value, current.next.value if current.next else None), end=' ')
        current = current.prev
    print()

iterateThroughListForwards(linkedList)

linkedList.remove(Node(1))
linkedList.remove(Node(2))
linkedList.setHead(Node(3))
linkedList.setTail(Node(4))
linkedList.insertBefore(Node(3), Node(2))
linkedList.insertAfter(Node(4), Node(5))
nodeThree = Node(3)
linkedList.bindNodes(linkedList.tail, nodeThree)
linkedList.tail = nodeThree
linkedList.insertAtPosition(1, Node(3))
linkedList.removeNodesWithValue(3)

iterateThroughListForwards(linkedList)
print(linkedList.containsNodeWithValue(6))

print('done')
