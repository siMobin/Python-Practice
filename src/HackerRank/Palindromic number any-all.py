# Palindromic number any/all
# x = input().split(" ")
# if all(int(i) >= 0 for i in x):
#     if any(i == i[::-1] for i in x):
#         print(True)
# else:
#     print(False)

x = input().split()
print(any(i == i[::-1] for i in x) if all(int(i) >= 0 for i in x) else False)
