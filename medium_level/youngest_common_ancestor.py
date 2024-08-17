# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(h) time | O(h) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneAncestors = getAncestors(descendantOne, topAncestor)
    descendantTwoAncestors = getAncestors(descendantTwo, topAncestor)
    shorterAncestralTree = descendantOneAncestors if len(descendantOneAncestors) <= len(descendantTwoAncestors) else descendantTwoAncestors
    index = 0
    youngestCommonAncestor = topAncestor
    while index < len(shorterAncestralTree):
        if descendantOneAncestors[len(descendantOneAncestors) - index - 1].name == descendantTwoAncestors[len(descendantTwoAncestors) - index - 1].name:
            youngestCommonAncestor = shorterAncestralTree[len(shorterAncestralTree) - index - 1]
            index += 1
        else:
            break
    return youngestCommonAncestor
        
def getAncestors(descendant, topAncestor):
    descendantAncestors = [descendant]
    nextAncestor = descendant
    while nextAncestor != None:
        if nextAncestor.ancestor:
            descendantAncestors.append(nextAncestor.ancestor)
        else:
            descendantAncestors.append(topAncestor)
        nextAncestor = nextAncestor.ancestor
    return descendantAncestors
  
# ******************* Optimal solution ******************** #

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# O(h) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    descendantOneAncestralDepth = getAncestralDepth(descendantOne)
    descendantTwoAncestralDepth = getAncestralDepth(descendantTwo)
    
    longerAncestralDepth = descendantOneAncestralDepth if descendantOneAncestralDepth >= descendantTwoAncestralDepth else descendantTwoAncestralDepth 
    shorterAncestralDepth = descendantOneAncestralDepth + descendantTwoAncestralDepth - longerAncestralDepth
    difference = longerAncestralDepth - shorterAncestralDepth
    
    deeperDescendant = descendantOne if descendantOneAncestralDepth >= descendantTwoAncestralDepth else descendantTwo
    higherDescendant = next(iter(set([descendantOne, descendantTwo]) - set([deeperDescendant])))
    
    level_ancestor = deeperDescendant
    for _ in range(difference):
        if deeperDescendant.ancestor:
            level_ancestor = deeperDescendant.ancestor
            deeperDescendant = level_ancestor
        else:
            level_ancestor = topAncestor
    
    while True:
        if level_ancestor.name == higherDescendant.name:
            return level_ancestor
        else:
            level_ancestor = level_ancestor.ancestor
            higherDescendant = higherDescendant.ancestor
        
def getAncestralDepth(descendant):
    depth = 0
    nextAncestor = descendant
    while nextAncestor.ancestor:
        nextAncestor = nextAncestor.ancestor
        depth += 1
    return depth
