def commonCharacters(strings):
    sets = [set(string) for string in strings]
    finalSet = sets[0]
    for s in sets[1:]:
        finalSet = finalSet.intersection(s)
    return finalSet
