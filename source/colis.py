import stripe

class Colis:
    def __init__(self, nom_espediteur,address_espediteur, nom_destinataire,address_destinataire, poids):
        self.nom_espediteur = nom_espediteur
        self.address_espediteur = address_espediteur
        self.nom_destinataire = nom_destinataire
        self.address_destinataire = address_destinataire
        self.poids = poids
        self.cout_livraison = 0  # Propriété pour le coût d'expédition, initialisée à 0 par défaut

    def calcul_cout_livraison(self):
        Frais_expédition_par_kg_ordinaire = 1000
        Frais_expédition_par_kg_fragile = 1500

        if int(self.poids) < 10:
            self.cout_livraison = self.poids * Frais_expédition_par_kg_fragile
        else:
            self.cout_livraison = self.poids * Frais_expédition_par_kg_ordinaire

    @staticmethod
    def check_infos_payement(card_number,exp_month,exp_year,cvc):
        if card_number and exp_month.isdigit() and exp_year.isdigit() and cvc:
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
        else:
            print("Le paiement a échoué. Veuillez réessayer.")

    def __str__(self):
        self.calcul_cout_livraison()  # Calcul du coût d'expédition
        return f"Colis de {self.nom_espediteur} à destination de {self.address_espediteur}, poids : {self.poids} kg, coût d'expédition : {self.cout_livraison} F CFA"