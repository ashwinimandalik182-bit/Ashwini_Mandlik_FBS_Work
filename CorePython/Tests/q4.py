
area = float(input("Enter area of one wall: "))
interior = float(input("Enter interior painting cost per sq.ft: "))
exterior = float(input("Enter exterior painting cost per sq.ft: "))
totalWalls = 6
interiorCost = area * totalWalls * interior
exteriorCost = area * totalWalls * exterior
totalCost = interiorCost + exteriorCost
print(f"Interior painting cost is {interiorCost}")
print(f"Exterior painting cost is {exteriorCost}")
print(f"Total painting cost is {totalCost}")
