import sqlite3

connection = sqlite3.connect("Python/TPs/TP4/EX1.db")

cursor = connection.cursor()

cursor.executescript("""
    DROP TABLE IF EXISTS Film;
    CREATE TABLE Film(
        idFilm INTEGER PRIMARY KEY AUTOINCREMENT,
        titre VARCHAR(255) NOT NULL
    );
""")

films = [(1,"Les evades"),(2,"Le parrain"),(3,"La vie de Pi")]

for film in films:
    cursor.execute(""" INSERT INTO Film (idFilm,titre) VALUES (?,?) """,film)



films = (
    {"idFilm" : 4, "titre" : "Chocolat"},
    {"idFilm" : 5, "titre" : "Scarface"},
    {"idFilm" : 6, "titre" : "Rango"},
)

cursor.executemany(""" INSERT INTO Film (idFilm,titre) VALUES (:idFilm,:titre) """,films)
cursor.execute("SELECT * FROM Film")
filmlist = cursor.fetchall()

for film in filmlist:
    print(str(film[0]) + "|" + film[1])
for film in filmlist:
    print(film[1])

cursor.executescript("""
    DROP TABLE IF EXISTS Acteurs;
    CREATE TABLE Acteurs(
        idActeur INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL
    );
""")

acteurs = [("Johnny", "Deep"),("Al", "Pacino"),("Suraj", "Sharma")]


for acteur in acteurs:
    cursor.execute(""" INSERT INTO Acteurs (prenom,nom) VALUES (?,?)""",acteur)

cursor.execute(""" SELECT nom FROM Acteurs """)
nomActeurs = cursor.fetchall()

for nom in nomActeurs:
    print(nom[0])


cursor.executescript("""
    DROP TABLE IF EXISTS Filmographie;
    CREATE TABLE Filmographie(
        fk_film INTEGER NOT NULL,
        fk_acteur INTEGER NOT NULL,
        FOREIGN KEY(fk_film) REFERENCES Film(idFilm),
        FOREIGN KEY(fk_acteur) REFERENCES Acteurs(idActeur)
    )
""")

filmographie = [(3,3),(2,2),(4,1),(5,2),(6,1)]

for filmograph in filmographie:
    cursor.execute(""" INSERT INTO Filmographie (fk_film,fk_acteur) VALUES (?,?)""",filmograph)

cursor.execute(""" SELECT Film.titre,Acteurs.nom,Acteurs.prenom FROM Film,Acteurs JOIN Filmographie ON Film.idFilm = Filmographie.fk_film AND Acteurs.idActeur = Filmographie.fk_acteur """)

cursor.execute(""" SELECT titre, nom , prenom FROM Filmographie JOIN FILM,Acteurs ON Film.idFilm = Filmographie.fk_film AND Acteurs.idActeur = Filmographie.fk_acteur""")

filmss = cursor.fetchall()
for film in filmss:
    print("Le film : " + film[0] + "est contient l'acteur : " + film[1] + " " + film[2])

cursor.close()
connection.commit()