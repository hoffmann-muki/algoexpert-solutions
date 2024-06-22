def majorityElement(array):
    total = sum(array)
    half_array = len(array) // 2
    for elem in array:
        diff = total - half_array * elem
        remainder = sum([x for x in array if x != elem])
        if diff > remainder:
            return elem
    
def majorityElement(array):
    i = 0
    n = len(array)
    maj_candidate = 0
    while i < n:
        sum = 1
        for j in range(i+1, n):
            if array[j] != array[i]:
                sum -= 1
            else:
                sum += 1
            if sum == 0:
                break
        if sum > 0:
            maj_candidate = array[i]
            break
        i += 1
    return maj_candidate

# best solution: O(1) space and O(n) time

def majorityElement(array):
    i = 0
    n = len(array)
    maj = array[0]
    while i < n-1:
        sum = 1
        maj = array[i]
        j = i
        while sum > 0 and j < n-1:
            j += 1
            sum += (1 if array[j] == maj else -1)
        if j < n-1:
            maj = array[j+1]
        i = j+1
    return maj
