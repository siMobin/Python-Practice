# Read input and split into lists
a = input().split()
b = input().split()

# Generate all pairs (x, y) where x is from list a and y is from list b
pairs = [(x, y) for x in a for y in b]

# Print the pairs in the required format
print(" ".join(f"({x}, {y})" for x, y in pairs))
