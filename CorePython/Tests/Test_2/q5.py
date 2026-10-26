p1=int(input("Enter the Price of Prod1:"))
p2=int(input("Enter the Price of Prod:"))
p3=int(input("Enter the Price of Prod1:"))
p4=int(input("Enter the Price of Prod1:"))
p5=int(input("Enter the Price of Prod1:"))
total = p1+p2+p3+p4+p5

gst=total*18/100
bill=total+gst
print("total before gst:",total)
print("gst(18%):",gst)
print("total bill:",bill)