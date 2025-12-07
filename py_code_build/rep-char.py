from itertools import groupby

def rep_char(s):
    if not s:
        return ""

    groups = [(char,len(list(group))) for char, group in groupby(s)]
    maxchar, maxgroup = max(groups, key=lambda x: x[1])
    return maxchar * maxgroup

print(rep_char("aaabbbccccccd"))


