# users.py
import sys
import re
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

    
    @staticmethod
    def validate_email(email):
        # Vérifier le format de l'e-mail à l'aide d'une expression régulière
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            return False

    
    def create_user(name, address, email, password):
        # Créer une connexion à la base de données
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        if User.validate_email(email) == False:
            return 0
        else:
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
        
    def update_user(self, name, address, email):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        #mettre à jour les informations de l'utilisateur
        cursor.execute('UPDATE users SET name=?, address=?, email=? WHERE id=?',
                        (name, address, email, self.id))
        connection.commit()
        connection.close()

        self.name = name
        self.address = address
        self.email = email
        print("Informations mises à jour avec succès!")

    @staticmethod
    def get_all_users():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        #récupérer tous les utilisateurs
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()

        connection.close()
        return users

    
    def login(email, password):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Exécuter la requête pour récupérer l'utilisateur avec l'e-mail spécifié
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user_data = cursor.fetchone()

        if user_data is not None:
            user = User(user_data[1], user_data[2], user_data[3], user_data[4])
            user.id = user_data[0]
            # Vérifier le mot de passe
            if user.password == password:
                print(f"Connexion réussie. Bienvenue, {user.name}!")
                return user
            else:
                print("Mot de passe incorrect. Veuillez réessayer.")
        else:
            print("Adresse e-mail non trouvée. Veuillez vous inscrire.")

        connection.close()
        return None