# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    n = len(string)
    longest = {'value': '', 'length': 0}
    for i in range(1, n+1):
        for j in range(i):
            if isPalindrome(string[j:i], i-j):
                if len(string[j:i]) > longest['length']:
                    longest = {'value': string[j:i], 'length': i-j}
    return longest['value']

def isPalindrome(string, length):
    i = 0
    while i < length//2:
        if string[i] != string[length-1-i]:
            return False
        i += 1
    return True
