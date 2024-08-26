# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
def solve(s):
    x = s.split(" ")
    print(len(x))
    for i in range(len(x)):
        x[i] = x[i].capitalize()
    # X = x[0].upper()
    y = " ".join(x)
    return y


s = input()
result = solve(s)
print(result)
