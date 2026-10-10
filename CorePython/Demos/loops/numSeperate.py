num = 372
s=0
while(num>0):
    digit = num % 10
    s+=digit
    #print("digit is ",digit)
    num = num // 10
    #print("Number is ", num)
print(f"Sum is {s}.")