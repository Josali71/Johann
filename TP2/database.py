import sqlite3

class Database :
    def __init__ (self) :
        self.connexion = sqlite3.connect('db_pokemon.db')
        self.cursor = self.connexion.cursor()

        self.cursor.execute ('''
        CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        heigth INTEGER,
        weight INTEGER,
        types TEXT,
        bmi FLOAT
        )
        ''')

        self.connexion.commit()

    def save_pokemon(self, formatted_data) :
        self.cursor.execute ('''
            INSERT INTO pokemon (id, name, height, weight, types, bmi)
            VALUES (?, ?, ?, ?, ?, ?)
        ''',(formatted_data["id"], formatted_data["name"], formatted_data["height"], formatted_data["weight"], formatted_data["types"], formatted_data["bmi"])
        )

        self.connexion.commit()