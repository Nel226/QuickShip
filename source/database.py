
import sqlite3

# Fonction pour établir la connexion à la base de données SQLite
def create_connection():
    return sqlite3.connect('database.db')

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

    connection.commit()
    connection.close()
