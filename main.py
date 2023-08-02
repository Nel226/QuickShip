# main.py
import sys
sys.path.append("..")

from source.users import User

def main():
    print("Bienvenue dans l'application QuickShip !")
    print("Veuillez vous inscrire pour commencer.")

    name = input("Nom complet: ")
    address = input("Adresse: ")
    email = input("Adresse e-mail: ")
    password = input("Mot de passe: ")

    new_user = User.create_user(name, address, email, password)
    print(f"Utilisateur enregistré avec l'ID : {new_user.id}")
    
    afficher_utilisateurs_enregistres()

def afficher_utilisateurs_enregistres():
    from source.users import users
    print("Liste des utilisateurs enregistrés")
    print(users)
    for user in users:
        print(f"ID: {user.id}, Nom: {user.name}, Adresse e-mail: {user.email}")

if __name__ == "__main__":
    main()
