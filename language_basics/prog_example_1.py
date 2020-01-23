


# Take Input from the user for RADIUS of a circle and calculate the its AREA and CIRCUMFERENCE

# Radius of circle = r

# PI = 3.1415

# Area of a circle = PI x r*r

# Circumference of a circle = 2 x PI x r




























circle_radius = float(input("Enter the radius of a circle: "))

PI = 3.1415

circle_area = PI * circle_radius ** 2
circle_circum = 2 * PI * circle_radius

print(f"Area of Circle: {circle_area:.2f} and its Circumference is: {circle_circum:.2f}")