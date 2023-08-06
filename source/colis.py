import sqlite3
from data.database import create_connection

class Colis:
    def __init__(self, nom_espediteur,address_espediteur, nom_destinataire,address_destinataire, poids):
        self.nom_espediteur = nom_espediteur
        self.address_espediteur = address_espediteur
        self.nom_destinataire = nom_destinataire
        self.address_destinataire = address_destinataire
        self.poids = poids
        self.cout_livraison = 0  # Propriété pour le coût d'expédition, initialisée à 0 par défaut

    def create_colis(nom_espediteur, address_espediteur, nom_destinataire, address_destinataire ,poids):
        # Créer une connexion à la base de données
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # Exécuter la requête pour insérer un nouvel utilisateur
        cursor.execute('INSERT INTO colis (nom_espediteur,address_espediteur,nom_destinataire,address_destinataire,poids) VALUES (?, ?, ?, ?, ?)',
                    (nom_espediteur,address_espediteur,nom_destinataire,address_destinataire,poids))
        colis_id = cursor.lastrowid

        # Enregistrer les changements dans la base de données et fermer la connexion
        connection.commit()
        connection.close()

        new_colis = Colis(nom_espediteur, address_espediteur,  nom_destinataire, address_destinataire,poids)
        new_colis.id = colis_id
        return new_colis
    
    @staticmethod
    def get_all_colis():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        #récupérer tous les utilisateurs
        cursor.execute('SELECT * FROM colis')
        users = cursor.fetchall()

        connection.close()
        return users

    def calcul_cout_livraison(self):
        Frais_expédition_par_kg_ordinaire = 1000
        Frais_expédition_par_kg_fragile = 1500

        if int(self.poids) < 10:
            self.cout_livraison = self.poids * Frais_expédition_par_kg_fragile
        else:
            self.cout_livraison = self.poids * Frais_expédition_par_kg_ordinaire
        return self.cout_livraison

    @staticmethod
    def check_infos_payement(card_number,exp_month,exp_year,cvc):
        if len(card_number)== 16 and exp_month.isdigit() and exp_year.isdigit() and len(cvc)==3 and 1 <= exp_month <= 12 and exp_year > 2023:
            return True
        else:
            return False
        


    def process_payment(self):
        print("Veuillez saisir les informations de paiement :")
        card_number = input("Numéro de carte de crédit : ")
        exp_month = input("Mois d'expiration (MM) : ")
        exp_year = input("Année d'expiration (YYYY) : ")
        cvc = input("Code de sécurité (CVC) : ")

        if Colis.check_infos_payement(card_number, exp_month, exp_year, cvc) == True:
            print("Le paiement a été effectué avec succès !")
            return True
        else:
            print("Le paiement a échoué. Veuillez réessayer.")
            return False

    def __str__(self):
        if self.process_payment() == True:
            return f"Colis de {self.nom_espediteur} à destination de {self.address_espediteur}, poids : {self.poids} kg, coût d'expédition : {self.calcul_cout_livraison()} F CFA"
        else:
            return 0