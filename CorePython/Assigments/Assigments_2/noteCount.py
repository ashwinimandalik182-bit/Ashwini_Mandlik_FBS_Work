amount = int(input("Enter amount: "))

n200 = amount // 200
amount = amount % 200

n50 = amount // 50
amount = amount % 50

n20 = amount // 20
amount = amount % 20

n10 = amount // 10
amount = amount % 10

n5 = amount // 5
amount = amount % 5

n2 = amount // 2
amount = amount % 2

n1 = amount // 1

total = n200 + n50 + n20 + n10 + n5 + n2 + n1

print("Minimum number of notes:", total)