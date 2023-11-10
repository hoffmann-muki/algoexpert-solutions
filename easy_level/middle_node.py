# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def middleNode(linkedList):
    if linkedList.next is None:
        return linkedList
    else:
        fast_ptr = linkedList
        slow_ptr = linkedList
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            if fast_ptr.next is not None:
                fast_ptr = fast_ptr.next.next
            else:
                fast_ptr = None
        return slow_ptr
