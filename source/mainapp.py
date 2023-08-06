import sys
import bcrypt
sys.path.append("..")
from source.users import User
from source.colis import Colis
from data.database import create_users_table, create_colis_table

# Créer la table "users" dans la base de données s'il n'existe pas déjà
create_users_table()
# Créer la table "COLIS" dans la base de données s'il n'existe pas déjà
create_colis_table()
class MainApp:
    def __init__(self):
        self.current_user = None

    def main_menu(self):
        print("\nMenu:")
        if self.current_user is None:
            print("1. Créer un nouvel utilisateur")
            print("2. Se connecter")
        else:
            print("3. Faire une commande")
            print("4. Afficher les utilisateurs")
            print("5. Se déconnecter")
            print("6. Historique de commande")

        print("7. Quitter")

        choice = input("Veuillez choisir une option (1-7) : ")
        return choice

    def register_user(self):
        print("Commencençons l'inscription.")
        name = input("Nom: ")
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

    def login(self):
        email = input("Adresse e-mail: ")
        password = input("Mot de passe: ")
        user = User.login(email, password)
        if user is not None:
            print(f"Connexion réussie. Bienvenue, {user.name}!")
            self.current_user = user

    def commande(self):
        print("Entrez les informations du colis!")
        nom_espediteur = input("Entrer votre nom:")
        address_espediteur = input("Entrez votre addresse:")
        nom_destinataire = input("Entrez le nom du destinataire:")
        address_destinataire = input("Entrez l'address du destinataire:")
        poids = input("Entrez le poids du colis")
        colis = Colis(
            nom_espediteur=nom_espediteur,
            address_espediteur=address_espediteur,
            nom_destinataire=nom_destinataire,
            address_destinataire=address_destinataire,
            poids=poids,
        )
        new_colis = Colis.create_colis(nom_espediteur, address_espediteur, nom_destinataire, address_destinataire,poids)
        colis.calcul_cout_livraison()

        # Traite le paiement
        colis.process_payment()

        # Affiche les informations du colis
        print(colis)

    def display_colis(self):
        colis = Colis.get_all_colis()
        for col in colis:
            print(f"nom espediteur: {col[0]}, address espediteur: {col[1]}, nom destinataire: {col[2]}, address destinateur: {col[3]}, poids: {col[4]}")


    def display_users(self):
        users = User.get_all_users()
        for user in users:
            print(f"ID: {user[0]}, Nom: {user[1]}, Adresse: {user[2]}, E-mail: {user[3]}")

    def logout(self):
        self.current_user = None

    def run(self):
        choice = self.main_menu()
        while True:
            if choice == "1":
                self.register_user()
                choice = self.main_menu()
            elif choice == "2":
                self.login()
                choice = self.main_menu()
            elif choice == "3" and self.current_user is not None:
                self.commande()
                choice = self.main_menu()
            elif choice == "4" and self.current_user is not None:
                self.display_users()
                choice = self.main_menu()
            elif choice == "5" and self.current_user is not None:
                self.logout()
                choice = self.main_menu()
            elif choice == "6" and self.current_user is not None:
                self.display_colis()
                choice = self.main_menu()
            elif choice == "7":
                print("Merci d'avoir utilisé notre service ! Au revoir.")
                break

            else:
                print("Option invalide. Veuillez choisir une option valide.")
