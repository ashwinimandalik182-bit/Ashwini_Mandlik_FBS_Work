num = int ( input ("Enter Number :"))

if num <= 1:
    print(f"{num} is Not Prime Number")
else:
    for i in range (2 , num):
        if num%i==0:
            print(f"{num} is Not Prime Number")
            break
    else:
        print(f"{num} is Prime Number")