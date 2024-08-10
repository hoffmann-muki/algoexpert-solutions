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
