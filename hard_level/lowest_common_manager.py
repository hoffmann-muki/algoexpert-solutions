# O(n) time | O(n) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    ancestralTree = { topManager.name: None }
    ancestralTree = getAncestralTree(topManager, ancestralTree)
    return getYoungestCommonAncestor(topManager, reportOne, reportTwo, ancestralTree)

# O(h) time | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo, ancestralTree):
    descendantOneAncestralDepth = getAncestralDepth(descendantOne, ancestralTree)
    descendantTwoAncestralDepth = getAncestralDepth(descendantTwo, ancestralTree)
    
    longerAncestralDepth = descendantOneAncestralDepth if descendantOneAncestralDepth >= descendantTwoAncestralDepth else descendantTwoAncestralDepth 
    shorterAncestralDepth = descendantOneAncestralDepth + descendantTwoAncestralDepth - longerAncestralDepth
    difference = longerAncestralDepth - shorterAncestralDepth
    
    deeperDescendant = descendantOne if descendantOneAncestralDepth >= descendantTwoAncestralDepth else descendantTwo
    higherDescendant = next(iter(set([descendantOne, descendantTwo]) - set([deeperDescendant])))
    
    level_ancestor = deeperDescendant
    for _ in range(difference):
        if ancestralTree[deeperDescendant.name]:
            level_ancestor = ancestralTree[deeperDescendant.name]
            deeperDescendant = level_ancestor
        else:
            level_ancestor = topAncestor
    
    while True:
        if level_ancestor.name == higherDescendant.name:
            return level_ancestor
        else:
            level_ancestor = ancestralTree[level_ancestor.name]
            higherDescendant = ancestralTree[higherDescendant.name]
        
def getAncestralDepth(descendant, ancestralTree):
    depth = 0
    nextAncestor = descendant
    while ancestralTree[nextAncestor.name]:
        nextAncestor = ancestralTree[nextAncestor.name]
        depth += 1
    return depth

def getAncestralTree(manager, ancestralTree):
    directReports = manager.directReports
    if directReports:
        for directReport in directReports:
            ancestralTree[directReport.name] = manager
            getAncestralTree(directReport, ancestralTree)
        return ancestralTree
    else:
        return ancestralTree

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
