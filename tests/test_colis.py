import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from source.colis import Colis

class TestColisMethods(unittest.TestCase):

    def test_create_colis(self):
        # Créer un colis de test
        colis = Colis.create_colis("SOME", "Bobo", "Judicael", "Karpala", 5.0)

        # Vérifier que le colis a été créé avec les bonnes valeurs
        self.assertEqual(colis.nom_espediteur, "SOME")
        self.assertEqual(colis.address_espediteur, "Bobo")
        self.assertEqual(colis.nom_destinataire, "Judicael")
        self.assertEqual(colis.address_destinataire, "Karpala")
        self.assertEqual(colis.poids, 5.0)
        self.assertEqual(colis.cout_livraison, 0)

    def test_get_all_colis(self):
        # Ajouter quelques colis de test à la base de données
        Colis.create_colis("SOME", "Bobo", "Bayala", "Reo", 7.0)
        Colis.create_colis("SOME", "Bobo", "Rachid", "Belle ville", 12.0)

        # Récupérer tous les colis
        Colis.get_all_colis()

    def test_calcul_cout_livraison(self):
        # Créer un colis de test
        colis = Colis("SOME", "Bobo", "Bayala", "Reo", 7)

        # Calculer le coût de livraison
        cout = colis.calcul_cout_livraison()

        # Vérifier que le coût calculé est correct
        self.assertEqual(cout, 10500)  # Le poids est inférieur à 10, donc coût_fragile

    def test_check_infos_payement(self):
        # Vérifier un exemple de carte de crédit valide
        self.assertTrue(Colis.check_infos_payement("1234567890123456", "12", "2024", "123"))

        # Vérifier un exemple de carte de crédit invalide
        self.assertFalse(Colis.check_infos_payement("1234567890123456", "15", "2022", "12"))

    def test_process_payment(self):
        # Créer un colis de test
        colis = Colis("SOME", "Bobo", "Bado", "Patte d'oie", 8.0)

        # Tester le processus de paiement avec des informations valides
        self.assertTrue(colis.process_payment())

        # Tester le processus de paiement avec des informations invalides
        self.assertFalse(colis.process_payment())
