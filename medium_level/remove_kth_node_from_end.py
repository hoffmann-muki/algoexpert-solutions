# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    size = 0
    current = head
    while current:
        size += 1
        current = current.next
    i = 0
    pointers = { 'previous': None, 'current': head }
    position = size - k
    while i < position:
        pointers['previous'] = pointers['current']
        pointers['current'] = pointers['current'].next
        i += 1
    if not pointers['previous']:
        if not pointers['current'].next:
            head = None
        else:
            head = pointers['current'].next
    else:
        if not pointers['current'].next:
            pointers['previous'].next = None
        else:
            pointers['previous'].next = pointers['current'].next
