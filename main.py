# main.py
import sys
sys.path.append("..")

from source.users import User
from source.database import create_users_table, create_connection  # Ajoutez "create_connection"

def main():
    # Créer la table "users" dans la base de données s'il n'existe pas déjà
    create_users_table()

    print("Bienvenue dans l'application QuickShip !")
    print("Veuillez vous inscrire pour commencer.")

    name = input("Nom complet: ")
    address = input("Adresse: ")
    email = input("Adresse e-mail: ")
    password = input("Mot de passe: ")

    new_user = User.create_user(name, address, email, password)
    print(f"Utilisateur enregistré avec l'ID : {new_user.id}")
    
    # Afficher la liste des utilisateurs enregistrés après l'enregistrement
    afficher_utilisateurs_enregistres()

def afficher_utilisateurs_enregistres():
    connection = create_connection()  # Utilisez la fonction pour établir la connexion
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    print("Liste des utilisateurs enregistrés :")
    for user in users:
        print(f"ID: {user[0]}, Nom: {user[1]}, Adresse e-mail: {user[3]}")

    connection.close()

if __name__ == "__main__":
    main()
