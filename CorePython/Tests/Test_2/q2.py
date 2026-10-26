#Write a program to accept 3 digit number. If first digit is double of second digit and half of
#third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
n= int(input ("Enter the number:"))
first=n//100
sec=(n//10)%10
third=n%10
if first == 2 *sec and first ==third /2 :
    print("Yes, you have done it")
else:
    print("Please try next time")