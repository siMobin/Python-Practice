# HackerRank is shit!

import inflect

p = inflect.engine()
n = int(input())

test_cases = []
for _ in range(n):
    x = int(input())
    test_cases.append(x)

for xx in test_cases:
    print(p.number_to_words(xx).replace("-", " ").replace(",", "").title())
