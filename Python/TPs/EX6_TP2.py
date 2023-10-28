num_trouver = int(input("Numero Trouver : Entrez un nombre entre 1 et 3 : "))
num = int(input("Votre Numero : Entrez un nombre entre 1 et 3 : "))

while num != num_trouver:
    if num < 1 or num > 3:
        print("Numero invalide")
        break
    if num < num_trouver:
        print("Trop petit")
    elif num > num_trouver:
        print("Trop grand")
    else:
        print("Bravo")
    num = int(input("Votre Numero : Entrez un nombre entre 1 et 3 : "))
    