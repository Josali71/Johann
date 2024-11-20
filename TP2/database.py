import sqlite3 # importe la bibliothèque SQLite3

class Database :
    def __init__ (self) :
        self.connexion = sqlite3.connect('db_pokemon.db', check_same_thread=False) # se connecte à la base db_pokemon.db, la crée si elle n'existe pas
        self.cursor = self.connexion.cursor() # permet l'alimentation de la base

# créée la table pokemon si elle n'existe pas et crée les champs qu'elle contient
        self.cursor.execute ('''
        CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        height INTEGER,
        weight INTEGER,
        types TEXT,
        bmi FLOAT
        )
        ''')

        self.connexion.commit() # enregistre la base avec les informations créées
        self.connexion.close()

    def save_pokemon(self, formatted_data) : # récupère les infos depuis formatted_date et les importe dans la bdd
        self.connexion = sqlite3.connect('db_pokemon.db', check_same_thread=False)
        self.cursor = self.connexion.cursor()
        try :
            self.cursor.execute ('''
                INSERT INTO pokemon (id, name, height, weight, types, bmi)
                VALUES (?, ?, ?, ?, ?, ?)
            ''',(formatted_data["id"], formatted_data["name"], formatted_data["height"], formatted_data["weight"], formatted_data["types"], formatted_data["bmi"])
            )

        except sqlite3.IntegrityError :
            print ("Ce pokemon est deja existant en bdd")

        self.connexion.commit()
        self.connexion.close()
        