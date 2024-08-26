# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
set_1 = set()
set_2 = set()

f = int(input())
x = input().split()
for i in range(f):
    for i in x:
        set_1.add(i)

g = int(input())
y = input().split()

for i in range(g):
    for i in y:
        set_2.add(i)

print(len(set().union(set_1, set_2)))
