from collections import Counter
s = "ABABCCCCC"
k = 2
counts = Counter()
res = lo = 0
for hi in range(len(s)):
    counts[s[hi]] += 1
    #counts[s[lo]] -= 1
    #print(counts)
    max_char_n = counts.most_common(1)[0][1]
    while hi - lo - max_char_n + 1 > k:
        print(hi)
        counts[s[lo]] -= 1
        lo += 1
    res = max(res, hi - lo + 1)
print(res)