# largest number
a = int(input("Enter The First Number : "))
b = int(input("Enter The Seceond Number : "))
c = int(input("Enter The Thard Number : "))

Max = max(a, b, c)
print("Largest Number Is :", Max)

print('##################  Seceond Program #################################')

if a >= b and a >= c:
    print("Largest Number is :", a)
elif b >= a and b >= c:
    print("Largest Number is :", b)
else:
    print("Largest Number is :", c)
