## prime number calculation program
a = int(input("Enter The Prime Number : "))
if a%1==0:
    if a%a==0:
     print("This is a prime number")
else:
    print("This is not prime number")