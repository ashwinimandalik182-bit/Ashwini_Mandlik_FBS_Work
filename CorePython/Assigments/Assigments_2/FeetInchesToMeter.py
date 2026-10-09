# Convert distant given in feet and inches into meter and centimeter.
feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

meter = feet * 0.3048 + inches * 0.0254
centimeter = feet * 30.48 + inches * 2.54

print("Distance in meter =", meter)
print("Distance in centimeter =", centimeter)