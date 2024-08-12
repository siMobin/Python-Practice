# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
s = input()

x = tuple(input().split(" "))

print(s.replace(s[int(x[0])], x[1]))
