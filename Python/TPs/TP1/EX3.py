import math

rayon = float(input("Saisir le rayon : "))
hauteur = float(input("Saisir la hauteur : "))
volume = (1/3) * math.pi * rayon**2 * hauteur
print("Le volume du cone droit est : ", volume)
