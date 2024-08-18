# O(n*w) time | O(n*w) space
def groupAnagrams(words):
    map = {}
    for string in words:
        uniqueString = arrangeLettersLexicographically(string)
        if uniqueString in map.keys():
            map[uniqueString].append(string)
        else:
            map[uniqueString] = [string]
    groups = []
    for key in map:
        groups.append(map[key])
    return groups

def arrangeLettersLexicographically(string):
    l = []
    for letter in string:
        l.append(letter)
    l.sort()
    return ''.join(l)
