# multiplication of unknown number
while True:
    a = int(input("Enter The Multiplication Number:"))
    i = 0
    for i in range(0, 10):
        i = i + 1
        print(a, "*", i, "=", i * a)
