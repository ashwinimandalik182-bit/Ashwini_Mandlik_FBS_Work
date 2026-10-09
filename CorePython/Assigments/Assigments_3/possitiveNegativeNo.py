# 1. Write a program to check if the given number is positive or negative.
num = int (input ("Enter Number:"))
if (num == 0):
    print("Neutral")
elif(num>0):
    print(f"{num} is Possitive Number!")
else:
    print(f"{num} is Negative Number!")