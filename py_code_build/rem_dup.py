def rem_dup(s):
    result_str = ""
    cleaned = set()
    for c in s:
        if c not in cleaned:
            result_str += c
            cleaned.add(c)

    return result_str
print(rem_dup("banana"))