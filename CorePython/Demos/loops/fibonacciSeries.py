n= int(input("Enter the Numbers:"))
a = -1
b=1
for i in range(n+1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c