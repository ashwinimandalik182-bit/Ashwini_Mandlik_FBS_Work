# 4. Write a program to enter P, T, R and calculate simple Interest.

p = int (input (" Enter the Principle Amount :"))
t = int (input ("Enter the Time :"))
r = int (input ("Enter the Rate of Intrest :"))
si=(p*t*r)/100
print(f"Simple Intrest = {si}")