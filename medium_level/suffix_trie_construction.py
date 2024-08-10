# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # O(n^2) time | O(n^2) space
    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    # O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

# ********** Recursive Solution *********** #

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        if len(string) == 0:
            return
        n = len(string)
        index = 0
        while index < n:
            key = string[index]
            if index == n-1:
                if key in self.root:
                    self.root[key][self.endSymbol] = True
                else:
                    self.root[key] = {self.endSymbol: True}
            else:
                if key in self.root:
                    self.root[key] = self.constructSuffixTrie(string, self.root[key], index+1, n)
                else:
                    self.root[key] = self.constructSuffixTrie(string, {}, index+1, n)
            index += 1
    
    def constructSuffixTrie(self, string, trie, index, n):
        if index == n:
            if len(trie) == 0:
                return {self.endSymbol: True} 
            else:
                return {string[index-1]: trie[string[index-1]], self.endSymbol: True}
        key = string[index]
        if len(trie) != 0:
            if key in trie:
                if self.endSymbol in trie[key]:
                    trie = {key: trie[key], self.endSymbol: True}
                    return trie
                else:
                    trie[key] = self.constructSuffixTrie(string, trie[key], index+1, n)
            else:
                trie[key] = self.constructSuffixTrie(string, {}, index+1, n)
            return trie
        else:
            trie[key] = self.constructSuffixTrie(string, {}, index+1, n)
            return trie

    # O(m) time | O(1) space
    def contains(self, string):
        n = len(string)
        index = 0
        dictionary = self.root
        while index < n:
            if string[index] not in dictionary:
                return False
            dictionary = dictionary[string[index]]
            index += 1
        return self.endSymbol in dictionary
