# Write a program to calculate the percentage of student based on marks of any 5 subjects.

s1=int(input("Enter the Subject 1 :"))
s2=int(input("Enter the Subject 2 :"))
s3=int(input("Enter the Subject 3 :"))
s4=int(input("Enter the Subject 4 :"))
s5=int(input("Enter the Subject 5 :"))
TotalMarks=s1+s2+s3+s4+s5
print(f"Total Marks Of Five Subject = {TotalMarks}")
per=(TotalMarks/500)*100
print(f"Percentage of Five Subject = {per}")