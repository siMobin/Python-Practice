# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
f = input().split(" ")
x, k = float(f[0]), float(f[1])

# Take the input for the polynomial expression
p = input().strip()

# Evaluate the expression with x as the variable
# Create a dictionary with x defined
context = {"x": x}

# Use eval with the provided context
px = eval(p, {}, context)

# Show the fuck'n result
if px == k:
    print("True")
else:
    print("False")
