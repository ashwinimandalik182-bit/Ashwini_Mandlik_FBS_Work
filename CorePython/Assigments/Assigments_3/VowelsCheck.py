# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

ch = input("Enter Character:")

vowels = 'a,e,i,o,u'

if ch in vowels:
    print("Vowels")
else:
    print("consonant")