# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
s1 = int ( input ("Enter sub1 marks :"))

s2 = int ( input ("Enter sub1 marks :"))

s3 = int ( input ("Enter sub1 marks :"))

s4 = int ( input ("Enter sub1 marks :"))

s5 = int ( input ("Enter sub1 marks :"))

marks = s1 + s2 + s3 + s4 + s5

per = marks / 5

if per >= 85 and per <= 100:

    print(f"O++ Grade with {per} %")

elif per >= 65 and per < 85:

    print(f"A Grade with {per} %")

elif per>50 and per < 65 :

    print(f"B Grade with {per} %")

elif per >= 35 and per <50:

    print(f"C Grade With {per} %")

else:

    print("Student is Fail. Study More!") 
