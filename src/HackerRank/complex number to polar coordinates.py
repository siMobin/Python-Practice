import cmath
import math

z = complex(input())

# Calculate magnitude and phase
r = abs(z)
theta = cmath.phase(z)

# Print results
print(r)
print(theta)

# Optionally, convert the angle to degrees if needed
# print(f"Angle (in degrees): {math.degrees(theta)}")
