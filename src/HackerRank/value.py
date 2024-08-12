# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
n = int(input())

data = {}  # dictionary
if n < 2 or n > 5:
    pass
else:
    for i in range(n):
        name = input()
        score = float(input())
        data[name] = score

# print("Original data:", data)

# Sort the dictionary by value (score) in descending order
sorted_data = sorted(data.items(), key=lambda item: (-item[1], item[0]))

# print("Sorted data:", sorted_data)

# Find the highest +1 score
highest_score = sorted_data[2][1]

# Print names with the 2nd highest score

for item in sorted_data:
    if item[1] == highest_score:
        print(item[0])
