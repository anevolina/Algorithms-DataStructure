
def KMP(string, pattern):

    helper = get_longest_prefix(pattern)

    pat_index = 0
    str_index = 0

    while str_index < len(string):
        if pattern[pat_index] == string[str_index]:
            pat_index += 1
            str_index += 1

        if pat_index == len(pattern):
            return str_index - pat_index

        elif str_index < len(string) and pattern[pat_index] != string[str_index]:
            if pat_index != 0:
                pat_index = helper[pat_index-1]
            else:
                str_index += 1
    return -1



def get_longest_prefix(pattern):
    prefix_current = 0
    sufix_current = 1
    table = [0]*len(pattern)

    while sufix_current < len(pattern):
        if pattern[prefix_current] == pattern[sufix_current]:
            table[sufix_current] = prefix_current + 1
            prefix_current += 1
            sufix_current += 1
        else:
            if prefix_current != 0:
                prefix_current = table[prefix_current-1]
            else:
                sufix_current += 1

    return table

print(KMP('abcdabcabceabcdedefsajkloooklsdswde', 'abcab'))
