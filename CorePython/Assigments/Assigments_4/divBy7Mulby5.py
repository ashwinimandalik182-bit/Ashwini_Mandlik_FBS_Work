n1 = int ( input (" Enter number:"))
n2 = int(input("Enter Number :"))
for i in range (n1,n2+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i)