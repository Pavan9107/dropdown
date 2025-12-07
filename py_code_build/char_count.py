s = "hello"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)


s = "hello"
freq = {}

for ch in s:
    found = False
    for key in freq:
        if ch == key:
            freq[key] = freq[key] + 1
            found = True
    if not found:
        freq[ch] = 1

print(freq)
