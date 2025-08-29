length = float(input("Enter the length:"))
breadth = float(input("Enter the breadth:"))
radius = float(input("Enter the radius:"))
Area = length * breadth
Circle_area = 3.14 * (radius ** 2)
total_area = Area + Circle_area
print("area of this figure is:", total_area)

p = 2 * (length + breadth)
circle_p = 3.14 * radius
total_perimeter = p + circle_p
print("Perimeter of this figure is:", total_perimeter)