
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))
age5 = int(input("Enter age of person 5: "))

ticket = float(input("Enter ticket amount per person: "))

if age1 < 12:
    t1 = ticket * 0.70
elif age1 > 59:
    t1 = ticket * 0.50
else:
    t1 = ticket

if age2 < 12:
    t2 = ticket * 0.70
elif age2 > 59:
    t2 = ticket * 0.50
else:
    t2 = ticket

if age3 < 12:
    t3 = ticket * 0.70
elif age3 > 59:
    t3 = ticket * 0.50
else:
    t3 = ticket

if age4 < 12:
    t4 = ticket * 0.70
elif age4 > 59:
    t4 = ticket * 0.50
else:
    t4 = ticket

if age5 < 12:
    t5 = ticket * 0.70
elif age5 > 59:
    t5 = ticket * 0.50
else:
    t5 = ticket

total = t1 + t2 + t3 + t4 + t5

print("Total ticket amount:", total)
