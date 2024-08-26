# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
s = input()

count = 1  # Initialize the count to 1
result = []  # List to store the result tuples

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        result.append((count, int(s[i])))  # Convert character to integer
        count = 1  # Reset count for the new character

# Append the last group
result.append((count, int(s[-1])))  # Convert character to integer

for r in result:
    print(r, end=" ")
