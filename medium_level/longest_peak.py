def longestPeak(array):
    count, start = 0, 0
    n = len(array)
    longest_peak_len = 0
    while start < n-2:
        peak, found_peak = find_ascending_sequence(array, start, n)
        if found_peak:
            end, found_end = find_descending_sequence(array, peak, n)
            if found_end:
                curr_peak_len = end-start+1
                longest_peak_len = curr_peak_len if curr_peak_len > longest_peak_len else longest_peak_len
        start += 1
    return longest_peak_len

def find_ascending_sequence(array, start, n):
    count = 0
    index = start
    while index < n-2 and array[index+1] > array[index]:
        count, index = count+1, index+1
    if index < n-1 and count >= 1: # we've reached a peak
        return index, True
    else:
        return -1, False
    
def find_descending_sequence(array, peak, n):
    count = 0
    index = peak
    while index < n-1 and array[index+1] < array[index]:
        count, index = count+1, index+1
    if index < n and count >=1: # we've hit the bottom
        return index, True
    else:
        return -1, False
