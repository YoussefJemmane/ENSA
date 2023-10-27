num1 = int(input("Saisi numero 1"))
num2 = int(input("Saisi numerp 2"))
op = input("Saisi l'operateur")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Division par zero impossible")
    else:
        print(num1 / num2)
else:
    print("Operateur non valide")
    