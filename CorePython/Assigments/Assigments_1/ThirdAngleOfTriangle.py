# Write a Program to input two angles from user and find third angle of the triangle.
angle1 = int (input ("Enter the Angle 1 :"))
angle2 = int (input ("Enter the Angle 2 :"))
ans = angle1 + angle2
angle3 = 180 - ans
print(f"ans:{ans}")
print(f"Third Angle of Triangle : {angle3}")