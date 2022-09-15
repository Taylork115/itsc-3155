firstnum = int(input("Please enter first number: "))
secondnum = int(input("Please enter second number: "))

z = range(firstnum, secondnum)
for n in z:
    if (n % 7 == 0) and (n % 5 !=0):
        print(n)