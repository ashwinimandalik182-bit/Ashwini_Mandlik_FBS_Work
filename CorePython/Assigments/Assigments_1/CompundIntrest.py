# 5. Write a program to enter P, T, R and calculate Compound Interest.

p = int (input (" Enter the Principle Amount :"))
t = int (input ("Enter the Time :"))
r = int (input ("Enter the Rate of Intrest :"))
ci = p * (1 + r / 100) ** t - p
print(f" Compound Intrest = {ci}")
