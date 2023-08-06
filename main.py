from source.mainapp import MainApp
from source.colis import Colis

if __name__ == "__main__":
    app = MainApp()
    app.run()



"""while True:
    choice = main_menu()
    if (choice == "2"):
        email = input("Adresse e-mail: ")
        password = input("Mot de passe: ")
        
        user = User.login(email, password)
        if user is not None:
            print(f"Connexion réussie. Bienvenue, {user.name}!")
            update = input("1 pour modifier 0 pour continuer et 3 pour payer")
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
            elif update == "3":
                print("Entrez les informations du colis!")
                nom_espediteur = input("Entrer votre nom:")
                address_espediteur = input("Entrez votre addresse:")
                nom_destinataire = input("Entrez le nom du destinataire")
                address_destinataire = input("Entrez l'address du destinataire")
                poids = input("Entrez le poids du colis")
                Colis = Colis(
                    nom_espediteur=nom_espediteur,
                    address_espediteur=nom_destinataire,
                    nom_destinataire=nom_destinataire,
                    address_destinataire=address_destinataire,
                    poids=poids,
                )
                Colis.calcul_cout_livraison()

                # Traite le paiement
                Colis.process_payment()

                # Affiche les informations du colis
                print(Colis)
            break
        else:
            print("La connexion a échoué. Veuillez vérifier vos informations de connexion.")

    elif(choice == "1"):
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
        print("Option  invalide ! Veuillez taper sur la touche 1 ou 2.")"""

