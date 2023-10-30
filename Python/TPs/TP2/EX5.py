notes = []
total_notes = int(input("Combien de notes voulez-vous saisir ? "))


for i in range(total_notes):
    
    note = float(input("Entrez une note : "))
    while note < 0 or note > 20:
        print("Note invalide")
        break
    notes.append(note)

print("La moyenne est de : ", sum(notes)/len(notes))

