a  = int ( input ("Enter Angle side:"))
b  = int ( input ("Enter Angle side:"))
c  = int ( input ("Enter Angle side:"))
if a + b > c and a + c > b and b + c > a :
    print("Valid ")
else:
    print("Not Valid")