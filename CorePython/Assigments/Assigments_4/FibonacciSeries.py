n = int ( input ("Enter Number :"))
a=-1
b=1
c=0
for i in range (n):
    c=a+b 
    a=b
    b=c
    print(c, end=" ")