cp = int ( input ("Enter Cost Price:"))
sp = int (input ("Enter Sells Price:"))
profit = sp - cp
loss = cp - sp
if (sp > cp):
    print(f"Profit {profit}")
elif ( cp>sp):
    print(f"Loss {loss}")
else:
    print("No Profit No Loss")