def count_vow(s):
    vow_count = 0
    cons_count = 0
    for char in s:
        if char.isalpha():
            vowel = "aeiouAEIOU"
            if char in vowel:
                vow_count += 1
            else:
                cons_count += 1
    return vow_count, cons_count
print(count_vow("HELLO"))

