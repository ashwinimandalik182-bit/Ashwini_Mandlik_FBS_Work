a  = int ( input ("Enter Angle side:"))
b  = int ( input ("Enter Angle side:"))
c  = int ( input ("Enter Angle side:"))
if a == b == c:
    print ("Equilateral Traingle")
elif a == b or b==c or c==a:
    print("Isosceles Triangle")
else:
    print("Traingle Scalene")