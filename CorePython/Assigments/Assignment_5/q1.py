# Q1
id="Admin"
passw="12345"

for i in range(3):
    userid = input("Enter Userid:")
    password = input("Enter Password:")

    if userid == id and password==passw:
        print("Login Successfull")
    else:
        print("Invalid ")

    if i==2:
        print("Your attempt Completed program is terminated ")
    else:
        print("try Again")