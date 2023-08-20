import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from source.colis import Colis



def test_create_colis():
    colis = Colis.create_colis("SOME", "Bobo", "Judicael", "Karpala", 5.0)
    assert colis.nom_espediteur == "SOME"
    assert colis.address_espediteur == "Bobo"
    assert colis.nom_destinataire == "Judicael"
    assert colis.address_destinataire == "Karpala"
    assert colis.poids == 5.0
    assert colis.cout_livraison == 0

def test_check_infos_payement():
    assert Colis.check_infos_payement("1234567890123456", "12", "2024", "123") == True
    assert Colis.check_infos_payement("1234567890123456", "15", "2022", "12") == False