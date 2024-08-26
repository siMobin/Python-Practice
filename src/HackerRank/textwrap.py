# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap


def wrap(string, max_width):
    x = textwrap.wrap(string, width=max_width)
    return "\n".join(x)


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# s = input()
# n = int(input())
# x = textwrap.wrap(s, width=n)

# # print(x)

# for i in x:
#     print(i)
