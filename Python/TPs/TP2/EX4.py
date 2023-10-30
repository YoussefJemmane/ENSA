N = int(input("Saisi un nombre"))

etat = True
for i in range(2,int(N/2)):
    if N % i == 0:
        etat = False
        break
    else:
        etat = True

if etat:
    print("Nombre premier")
else:
    print("Nombre non premier")