# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) time | O(max(n,m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    numberOne = getNumberSequence(linkedListOne)
    numberTwo = getNumberSequence(linkedListTwo)
    resultSequence = str(numberOne + numberTwo)
    resultSequence = resultSequence[::-1]
    n = len(resultSequence)
    linkedList = LinkedList(int(resultSequence[0]))
    current = linkedList
    index = 1
    while index < n:
        current.next = LinkedList(int(resultSequence[index]))
        current = current.next
        index += 1
    return linkedList

def getNumberSequence(linkedList):
    current = linkedList
    sequence = ''
    while current:
        sequence += str(current.value)
        current = current.next
    return int(sequence[::-1])
