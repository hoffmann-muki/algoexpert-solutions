def semordnilap(words):
    results = []
    word_dictionary = dict()
    # build the dictionary
    for word in words:
        l = ''.join(sorted(word))
        if l not in word_dictionary.keys():
            word_dictionary[l] = [words.index(word)]
        else:
            word_dictionary[l] += [words.index(word)]
    # get the semordnilap pairs
    for word in word_dictionary.keys():
        word_positions = word_dictionary[word]
        if len(word_positions) < 2:
            continue
        candidates = [words[pos] for pos in word_positions]
        if are_palindromes(candidates):
            results += [candidates]
    return results

def are_palindromes(candidates):
    if len(candidates) > 2:
        return False
    first, second = candidates[0], candidates[1]
    len_first, len_second = len(first), len(second)
    if len_first != len_second:
        return False
    for i in range(len_first):
        if first[i] != second[len_first-1-i]:
            return False
    return True
