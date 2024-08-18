# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n,m)) time | O(1) space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    listOneLength = 0
    listTwoLength = 0
    listOnePointer = linkedListOne
    listTwoPointer = linkedListTwo
    while listOnePointer is not None or listTwoPointer is not None:
        if listOnePointer:
            listOneLength += 1
            listOnePointer = listOnePointer.next
        if listTwoPointer:
            listTwoLength += 1
            listTwoPointer = listTwoPointer.next

    if listOneLength == listTwoLength:
        shorterListPointer = linkedListOne
        longerListPointer = linkedListTwo
    else:
        longerList = linkedListOne if listOneLength >= listTwoLength else linkedListTwo
        shorterList = next(iter(set([linkedListOne, linkedListTwo]) - set([longerList])))
        longerListLength = listOneLength if listOneLength >= listTwoLength else listTwoLength
        shorterListLength = (listOneLength + listTwoLength) - longerListLength
        difference = longerListLength - shorterListLength
        shorterListPointer = shorterList
        longerListPointer = longerList
        for _ in range(difference):
            longerListPointer = longerListPointer.next
    
    # parity achieved
    while shorterListPointer is not None:
        if shorterListPointer.value == longerListPointer.value:
            return shorterListPointer
        else:
            shorterListPointer = shorterListPointer.next
            longerListPointer = longerListPointer.next
    return None
