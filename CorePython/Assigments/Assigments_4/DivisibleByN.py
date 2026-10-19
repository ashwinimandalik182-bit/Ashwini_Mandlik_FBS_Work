start = int ( input ("enter Starting Number:"))
end  = int ( input ("enter Ending Number:"))
num =   int ( input ("enter Number:"))
for i in range (start, end+1):
    if  i % num == 0:
        print(i, end=" ")
       