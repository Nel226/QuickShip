# users.py
import sys
sys.path.append("..")
import sqlite3
from data.database import create_connection

class User:
    def __init__(self, name, address, email, password):
        self.id = None
        self.name = name
        self.address = address
        self.email = email
        self.password = password

    
    def create_user(name, address, email, password):
        # Créer une connexion à la base de données
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Exécuter la requête pour insérer un nouvel utilisateur
        cursor.execute('INSERT INTO users (name, address, email, password) VALUES (?, ?, ?, ?)',
                       (name, address, email, password))
        user_id = cursor.lastrowid

        # Enregistrer les changements dans la base de données et fermer la connexion
        connection.commit()
        connection.close()

        new_user = User(name, address, email, password)
        new_user.id = user_id
        return new_user
    
    def login(email, password):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Exécuter la requête pour récupérer l'utilisateur avec l'e-mail spécifié
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()

        if user is not None:
            # Vérifier le mot de passe
            if user[4] == password:
                print(f"Connexion réussie. Bienvenue, {user[1]}!")
                return user
            else:
                print("Mot de passe incorrect. Veuillez réessayer.")
        else:
            print("Adresse e-mail non trouvée. Veuillez vous inscrire.")

        connection.close()
        return None