# main.py
import sys
sys.path.append("..")
from source.users import User
from data.database import create_users_table

# Créer la table "users" dans la base de données s'il n'existe pas déjà
create_users_table()

print("Bienvenue dans l'application QuickShip !")
while True:
    have_compte=input(" Tapez sur la touche 1 pour vous connecter si vous avez déjà un compte, sinon tapez sur 2 pour vous inscrire :")
    if (have_compte == "1"):
        email = input("Adresse e-mail: ")
        password = input("Mot de passe: ")
        
        user = User.login(email, password)
        if user is not None:
            print(f"Connexion réussie. Bienvenue, {user[1]}!")
            break
        else:
            print("La connexion a échoué. Veuillez vérifier vos informations de connexion.")

    elif(have_compte=="2"):
        print("Commencençons l'inscription.")
        name = input("Nom: ")
        firstname = input ("Prénom")
        address = input("Adresse: ")
        email = input("Adresse e-mail: ")
        password = input("Mot de passe: ")

        new_user = User.create_user(name, address, email, password)
        print(f"Utilisateur enregistré avec l'ID : {new_user.id}")
        break
    else:
        print("Option  invalide ! Veuillez taper sur la touche 1 ou 2.")

