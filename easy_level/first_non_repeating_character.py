from collections import Counter

def firstNonRepeatingCharacter(string):
    counter = Counter(string)
    for letter in string:
        if counter.get(letter) == 1:
            return string.find(letter)
    return -1
