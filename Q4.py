l1 = int(input("Enter the length:"))
b1 = int(input("Enter the breadth:"))
h1 = int(input("Enter the heigth:"))

l2 = int(input("Enter the length:"))
b2 = int(input("Enter the breadth:"))
h1 = int(input("Enter the heigth:"))
cost_interior = int(input("Enter the cost_interior rate:" ))
cost_exterior = int(input("Enter the cost_exterior rate:"))

area1 = 2 * h1 * (l1 + b1)
area2 = 2 * h1 * (l2 + b2)
breadth_common = min(b1, b2)
common_wall_area = h1 * breadth_common

total_interior_area = area1 + area2 - common_wall_area
total_exterior_area = total_interior_area

interior_cost = total_interior_area * cost_interior
exterior_cost = total_exterior_area * cost_exterior
print("The interior cost of room is:",interior_cost)
print("The exterior cost of the room is:",exterior_cost)