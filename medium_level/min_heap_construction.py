# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        n = len(array)
        currentParent = (n-1) // 2
        while currentParent >= 0:
            self.siftDown(currentParent, array)
            currentParent -= 1
        return array

    # O(logn) time | O(1) space
    def siftDown(self, index, array):
        n = len(array)
        if index == n-1:
            return
        elementIdx = index
        leftChildIdx = 2*elementIdx + 1
        rightChildIdx = 2*elementIdx + 2
        while leftChildIdx < n:
            if rightChildIdx < n:
                if array[elementIdx] >= array[leftChildIdx] or array[elementIdx] >= array[rightChildIdx]:
                    smallerChildIdx = leftChildIdx if array[leftChildIdx] <= array[rightChildIdx] else rightChildIdx
                    self.swap(elementIdx, smallerChildIdx, array)
                    elementIdx = smallerChildIdx
                    leftChildIdx = 2*elementIdx + 1
                    rightChildIdx = 2*elementIdx + 2
                else:
                    return
            else: # missing right child
                if array[elementIdx] >= array[leftChildIdx]:
                    self.swap(elementIdx, leftChildIdx, array)
                    break
                else:
                    return

    # O(logn) time | O(1) space
    def siftUp(self, index, array):
        if index == 0:
            return
        elementIdx = index
        parentIdx = (elementIdx-1) // 2
        while array[elementIdx] < array[parentIdx] and elementIdx > 0:
            self.swap(elementIdx, parentIdx, array)
            elementIdx = parentIdx
            parentIdx = (elementIdx-1) // 2

    # O(1) time | O(1) space
    def swap(self, indexOne, indexTwo, array):
        if indexOne == indexTwo:
            return
        tmp = array[indexOne]
        array[indexOne] = array[indexTwo]
        array[indexTwo] = tmp

    # O(1) time | O(1) space
    def peek(self):
        if not self.heap:
            return
        else:
            return self.heap[0]

    # O(logn) time | O(1) space
    def remove(self):
        if not self.heap:
            return
        else:
            n = len(self.heap)
            value = self.heap[0]
            self.swap(0, n-1, self.heap)
            del self.heap[-1]
            if self.heap:
                self.siftDown(0, self.heap)
            return value

    # O(logn) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        n = len(self.heap)
        self.siftUp(n-1, self.heap)
