# main.py
import sys
import bcrypt
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
            print(f"Connexion réussie. Bienvenue, {user.name}!")
            update = input("1 pour modifier 0 pour continuer")
            if update == "1":
                name = input("Nom: ")
                firstname = input ("Prénom:")
                address = input("Adresse: ")
                email = input("Adresse e-mail: ")
                user.update_user(name=name, address=address, email=email)
            elif update == "0":
                users = User.get_all_users()
                for user in users:
                    print(f"ID: {user[0]}, Nom: {user[1]}, Adresse: {user[2]}, E-mail: {user[3]}")
            break
        else:
            print("La connexion a échoué. Veuillez vérifier vos informations de connexion.")

    elif(have_compte=="2"):
        print("Commencençons l'inscription.")
        name = input("Nom: ")
        firstname = input ("Prénom:")
        address = input("Adresse: ")
        email = input("Adresse e-mail: ")
        password = input("Mot de passe: ")

        if not name or not address or not email or not password:
            print("Tous les champs obligatoires doivent être remplis.")
        elif User.create_user(name, address, email, password) == 0:
            print("L'addresse mail est incorrecte")
        else:
            new_user = User.create_user(name, address, email, password)
            print(f"Utilisateur enregistré avec l'ID : {new_user.id}")
            break
    else:
        print("Option  invalide ! Veuillez taper sur la touche 1 ou 2.")

