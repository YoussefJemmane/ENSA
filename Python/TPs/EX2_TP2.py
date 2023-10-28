note = float(input("Entrez une note : "))

if note >= 0 and note < 10 :
    print("Insuffisant")
elif note >= 10 and note <12 :
    print("Passable")
elif note >= 12 and note <14 :
    print("Assez bien")
elif note >= 14 and note <16 :
    print("Bien")
elif note >= 16 and note <18 :
    print("Tres bien")
elif note >= 18 and note <=20 :
    print("Excellent")
else:
    print("Note non valide")