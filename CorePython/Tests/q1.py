
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
r = int(input("Enter the radius: "))

area = (l * b) + (3.14 * r * r / 2)
perimeter = (2 * l) + b + (3.14 * r)

print(f"Area of Figure is {area}.")
print(f"Perimeter of Figure is {perimeter}.")
