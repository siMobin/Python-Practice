# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):

    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()
    return "".join(s)


s = input()
result = swap_case(s)
print(result)
