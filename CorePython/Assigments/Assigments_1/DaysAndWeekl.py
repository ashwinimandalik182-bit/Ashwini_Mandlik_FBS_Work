# 8. Write a program to convert days into years, weeks and days.

days = int (input ("Enter Days :"))

year = days // 365

remaining_days = days % 365

weeks = remaining_days // 7

remaining_days = remaining_days % 7

print(f"Years :{year}")

print(f"Weeks :{weeks}")

print(f"remainig Days : {remaining_days}")