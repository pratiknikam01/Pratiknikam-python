height = float(input("Enter height: "))
width = float(input("Enter width: "))
depth = float(input("Enter depth: "))

dimensions = (height, width, depth)

height, width, depth = dimensions

volume = height * width * depth

print("Container dimensions:", dimensions)
print("Total volume:", volume, "cubic units")