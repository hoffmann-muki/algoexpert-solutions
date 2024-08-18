# O(2^n time) | O(n*2^n) space
def powerset(array):
    powerset = createPowerSet(frozenset([]), set(array), set([]))
    return [[]] + [list(fs) for fs in powerset]

def createPowerSet(currentSet, totalSet, powerset):
    if len(currentSet) > 0 and len(currentSet) == len(totalSet):
        return powerset
    remainder = totalSet - currentSet
    for element in remainder:
        newSet = currentSet.union(set([element]))
        if newSet not in powerset:
            powerset.add(newSet)
        createPowerSet(newSet, totalSet, powerset)
    return powerset
