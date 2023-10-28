numero = str(input("entrer un numero"))

etat = 1
for i in range(len(numero)):
    if numero.count(numero[i]) > 1:
        etat = 0
        
if etat == 1:
    print("le numero est distinct")
else:
    print("le numero n'est pas distinct")

    