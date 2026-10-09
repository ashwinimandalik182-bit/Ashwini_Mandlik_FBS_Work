# Discount = CP × Discount% / 100

# Selling Price = CP − Discount

cp = int (input("Enter the Cost Price :"))

discount = float (input ("Enter the Discount Percentage :"))

discount_amt = cp * discount / 100

sp = cp - discount_amt

print(f"Selling Price Of Book : {sp}.") 