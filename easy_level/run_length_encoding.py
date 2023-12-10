def runLengthEncoding(string):
    len_string = len(string)
    groups = split_into_groups(string)
    res = []
    for group in groups:
        encoded_str = get_run_length_encoding(group)
        res.append(encoded_str)
    return ''.join(res)

def split_into_groups(string):
    n = len(string)
    res = []
    curr_index= 0
    while curr_index <= n-1:
        substr = ''
        while curr_index <= n-2 and string[curr_index] == string[curr_index+1]:
            substr += string[curr_index]
            curr_index += 1
        substr += string[curr_index]
        res += [substr]
        curr_index += 1
    return res

def get_run_length_encoding(group):
    char = group[0]
    n = len(group)
    print(n)
    res = ''
    remainder = n
    while remainder > 10:
        res += '9' + char
        remainder -= 9
    res += str(remainder) + char
    return res
