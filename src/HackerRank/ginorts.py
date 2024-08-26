# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
s = input()
s = sorted(
    s,
    key=lambda x: (
        x.isdigit(),
        x.isdigit() and int(x) % 2 == 0,
        x.isupper(),
        x.islower(),
        x,
    ),
)

print("".join(s))
