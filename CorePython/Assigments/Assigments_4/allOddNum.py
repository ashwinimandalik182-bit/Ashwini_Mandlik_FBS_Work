n = int (input ("Enter Numbers :"))
count=0
for i in range (1 , n+1, 2):
    count+=1
    print(i,end=" ")
print("\nTotal Odd Numbers Count :",count)