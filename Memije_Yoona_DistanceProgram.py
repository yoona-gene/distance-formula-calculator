import math

# Points of the first coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Points of the second coordinate
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Output
print("The distance between 2 points is:", distance)
