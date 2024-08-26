n = int(input())
s_set = set()
for i in range(n):
    s = input()
    if s in s_set:
        s_set.remove(s)
        s_set.add(s)  # Fuck'n duplicate
    else:
        s_set.add(s)

print(len(s_set))
