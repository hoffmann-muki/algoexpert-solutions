# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeDuplicatesFromLinkedList(linkedList):
    curr = linkedList
    while curr is not None:
        if curr.next is None:
            return linkedList
        else:
            curr = removeDuplicatesFrom(curr)
        curr = curr.next
    return linkedList
    
# returns curr when its next value is different from the current one
def removeDuplicatesFrom(curr):
    next = curr.next
    while next is not None and curr.value == next.value:
        next_node = next.next
        if next_node is not None:
            curr.next = next_node
        else:
            curr.next = None
        next = curr.next
    return curr
