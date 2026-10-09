import random

userid = input ("Enter Userid :")
password = input ("Enter Password:")
if userid == 'Admin' and password == '1234':
    number = random.randint(1000,9999)
    print("Your captcha is ",number)

    captcha = int (input ("Enter Your Captcha :"))

    if captcha == number:
        print("Success ")
    else :
        print("Invalid")
