# best solution with O(n) space and O(nlogn) time

def mergeOverlappingIntervals(intervals):
    result = []
    intervals.sort()
    n = len(intervals)
    for i in range(n):
        curr = intervals[i]
        result = mergeIntervals(result, curr)
    return result

def mergeIntervals(result, curr):
    if len(result) == 0:
        return [[curr[0], curr[1]]]
    else:
        last = merge(result[-1], curr)
        if len(last) > 1:
            result = result[:-1] + last
        else:
            result[-1] = last[0]
        return result

def merge(first, second):
    first_begin, first_end = first
    second_begin, second_end = second
    if first_end < second_begin: # they are non-overlapping
        return [first, second]
    else:
        return [[first_begin, max(first_end, second_end)]]
