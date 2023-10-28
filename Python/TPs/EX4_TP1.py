a = int(input("a = "))
b = int(input("b = "))

if a * b > 0:
    a, b = b, a
    print("a = ", a, "b = ", b)
else:
    a, b = a + b, a * b
    print("a = ", a, "b = ", b)
