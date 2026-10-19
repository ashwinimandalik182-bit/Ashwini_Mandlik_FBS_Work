n = int ( input (" Enter Number :"))
if n<=0:
    print("Not Prime Number")
else:
    for i in range(2, n):
        if n % i ==0:
            print(f"{n} is Not Prime Number")
            break
    else:
        print(f"{n} is Prime Number")