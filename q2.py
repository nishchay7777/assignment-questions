from itertools import groupby

s = input()

compressed = []
for k, g in groupby(s):
    count = len(list(g))
    compressed.append(f"({count}, {k})")

print(" ".join(compressed))

