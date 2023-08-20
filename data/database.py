# database.py
import sqlite3

# Fonction pour établir la connexion à la base de données SQLite
def create_connection():
    return sqlite3.connect('database.db')
("Ouango Bénédicte", "Bobo", "nouveauemail@gmail.com")
# Fonction pour créer la table "users" dans la base de données
def create_users_table():
    connection = create_connection()
    cursor = connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        );
    '''
    cursor.execute(create_table_query)
    # Ajoutez un utilisateur initial à la table users
    cursor.execute('''
        INSERT INTO users (name, address, email, password)
        VALUES (?, ?, ?, ?)
    ''', ('Ouango Coco', 'Ouaga', 'coco@gmail.com', '1234'))
    connection.commit()
    connection.close()

# Fonction pour créer la table "colis" dans la base de données
def create_colis_table():
    connection = create_connection()
    cursor = connection.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS colis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom_espediteur TEXT NOT NULL,
            address_espediteur TEXT NOT NULL,
            nom_destinataire TEXT NOT NULL,
            address_destinataire TEXT NOT NULL,
            poids REAL NOT NULL
        );
    '''
    cursor.execute(create_table_query)

    connection.commit()
    connection.close()
