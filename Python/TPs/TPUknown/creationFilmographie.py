import sqlite3

def create_film_table(cursor):
    cursor.executescript("""
        DROP TABLE IF EXISTS Film;
        CREATE TABLE Film(
            idFilm INTEGER PRIMARY KEY AUTOINCREMENT,
            titre VARCHAR(255) NOT NULL
        );
    """)

def create_acteurs_table(cursor):
    cursor.executescript("""
        DROP TABLE IF EXISTS Acteurs;
        CREATE TABLE Acteurs(
            idActeur INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL
        );
    """)

def create_filmographie_table(cursor):
    cursor.executescript("""
        DROP TABLE IF EXISTS Filmographie;
        CREATE TABLE Filmographie(
            fk_film INTEGER NOT NULL,
            fk_acteur INTEGER NOT NULL,
            FOREIGN KEY(fk_film) REFERENCES Film(idFilm),
            FOREIGN KEY(fk_acteur) REFERENCES Acteurs(idActeur)
        );
    """)

def add_films(cursor, num_films):
    films = []
    for _ in range(num_films):
        film = input("Enter The Name of The Film: ")
        films.append((len(films) + 1, film))

    for film in films:
        cursor.execute("""INSERT INTO Film (idFilm, titre) VALUES (?, ?)""", film)

    return films

def add_acteurs(cursor, num_actors):
    acteurs = []
    for _ in range(num_actors):
        actor_first_name = input("Enter The First Name of The Actor: ")
        actor_last_name = input("Enter The Last Name of The Actor: ")
        acteurs.append((len(acteurs) + 1, actor_first_name, actor_last_name))

    for acteur in acteurs:
        cursor.execute("""INSERT INTO Acteurs (idActeur, prenom, nom) VALUES (?, ?, ?)""", acteur)

    return acteurs

def add_to_filmographie(cursor, films, acteurs):
    filmographie = []
    
    print("Films:")
    for i, film in enumerate(films):
        print(f"Film {i + 1}: {film[1]}")

    print("Acteurs:")
    for i, acteur in enumerate(acteurs):
        print(f"Actor {i + 1}: {acteur[1]} {acteur[2]}")

    fk_film = int(input("What's the film index you want to add to Filmographie? "))
    fk_acteur = int(input("What's the actor index for the selected film? "))

    filmographie.append((fk_film, fk_acteur))
    
    for filmograph in filmographie:
        cursor.execute("""INSERT INTO Filmographie (fk_film, fk_acteur) VALUES (?, ?)""", filmograph)

def main():
    connection = sqlite3.connect("Python/TPs/TPUknown/creationFilmographie.db")
    cursor = connection.cursor()

    create_film_table(cursor)
    num_films = int(input("Enter How Many Films do You Want to add: "))
    films = add_films(cursor, num_films)

    create_acteurs_table(cursor)
    num_actors = int(input("Enter How Many Actors do You Want to add: "))
    acteurs = add_acteurs(cursor, num_actors)

    create_filmographie_table(cursor)
    add_to_filmographie(cursor, films, acteurs)

    cursor.execute("""SELECT Film.titre, Acteurs.nom, Acteurs.prenom 
                      FROM Film, Acteurs 
                      JOIN Filmographie ON Film.idFilm = Filmographie.fk_film 
                      AND Acteurs.idActeur = Filmographie.fk_acteur""")
    
    film_list = cursor.fetchall()
    
    for film in film_list:
        print(f"Le film: {film[0]} met en scène l'acteur: {film[2]} {film[1]}")

    cursor.close()
    connection.commit()

if __name__ == "__main__":
    main()
