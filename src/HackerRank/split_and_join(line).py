# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
def split_and_join(line):
    x = line.split(" ")
    y = "-".join(x)
    return y


line = input()
result = split_and_join(line)
print(result)
