# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
n = int(input())

z = []
for i in range(n):
    x = input()
    k = x.split()
    # Add only non-empty strings to z
    if len(k) > 1:
        z.append(x)

for i in z:
    # i = i.replace(":", " ")
    # i = i.replace(",", " ")
    # i = i.replace(";", " ")
    # i = i.replace("(", " ")
    # i = i.replace(")", " ")
    i = i.translate(
        str.maketrans(",();:-_/*", "         ")
    )  # Use translate to remove unwanted characters...WTF
    f = i.split(" ")
    for j in f:
        if j.startswith("#"):
            print(j)
