'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.
'''

# Formula : Volume = πr2h
# Formula : Surface area = 2πr(h + r)

radius = 3.14
height = 5.0
PI = 3.1416
volume = PI * radius ** 2 * height
surface_area = 2 * PI * radius * (height + radius)

print(f"The Volume of the cylinder is {volume}")

print(f"The Surface area of the cylinder is {surface_area}")



