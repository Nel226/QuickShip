import sys
sys.path.append("..")
import pytest
from source.colis import Colis

def test_create_colis():
    # Créer un colis de test
    colis = Colis.create_colis("SOME", "Bobo", "Judicael", "Karpala", 5.0)

    # Vérifier que le colis a été créé avec les bonnes valeurs
    assert colis.nom_espediteur == "SOME"
    assert colis.address_espediteur == "Bobo"
    assert colis.nom_destinataire == "Judicael"
    assert colis.address_destinataire == "Karpala"
    assert colis.poids == 5.0
    assert colis.cout_livraison == 7500  # Le poids est inférieur à 10, donc coût_fragile

def test_get_all_colis():
    # Ajouter quelques colis de test à la base de données
    colis1 = Colis.create_colis("SOME", "Bobo", "Bayala", "Reo", 7.0)
    colis2 = Colis.create_colis("SOME", "Bobo", "Rachid", "Belle ville", 12.0)

    # Récupérer tous les colis
    colis_list = Colis.get_all_colis()

    # Vérifier que les colis ajoutés sont présents dans la liste
    assert colis1 in colis_list
    assert colis2 in colis_list

def test_calcul_cout_livraison():
    # Créer un colis de test
    colis = Colis("SOME", "Bobo", "CORNELIE", "Koupela", 8.0)

    # Calculer le coût de livraison
    cout = colis.calcul_cout_livraison()

    # Vérifier que le coût calculé est correct
    assert cout == 8000  # Le poids est inférieur à 10, donc coût_fragile

def test_check_infos_payement():
    # Vérifier un exemple de carte de crédit valide
    assert Colis.check_infos_payement("1234567890123456", "12", "2024", "123")

    # Vérifier un exemple de carte de crédit invalide
    assert not Colis.check_infos_payement("1234567890123456", "15", "2022", "12")

def test_process_payment():
    # Créer un colis de test
    colis = Colis("SOME", "Bobo", "Bado", "Patte d'oie", 8.0)

    # Tester le processus de paiement avec des informations valides
    assert colis.process_payment()

    # Tester le processus de paiement avec des informations invalides
    assert not colis.process_payment()
