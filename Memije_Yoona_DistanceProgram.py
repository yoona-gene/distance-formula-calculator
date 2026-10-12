import math

# Points of the first coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Points of the second coordinate
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Formula needed to calculate the distance between two points
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Result with the appropriate output message
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
