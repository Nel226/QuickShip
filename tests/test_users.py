import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), "..")))
from source.users import User
import pytest

# Test de la méthode validate_email
def test_validate_email_valid():
    assert User.validate_email("user@example.com") is None

def test_validate_email_invalid():
    assert User.validate_email("invalid-email") == False

# Test de la méthode create_user
def test_create_user_valid_email():
    user = User.create_user("Sy Rachid", "Rue 234,Bobo", "rachid@gmail.com", "password")
    assert user is not None

def test_create_user_invalid_email():
    user = User.create_user("Ouago Coco", "Rue 234, Ouaga", "invalid-email", "password")
    assert user == 0

# Test de la méthode update_user
def test_update_user():
    
    test_user = User("Ouango", "Ouaga", "coco@gmail.com", "password")
    test_user.id = 1  
    test_user.update_user("Ouango Bénédicte", "Bobo", "nouveauemail@gmail.com")
    
   
    updated_user_data = User.get_all_users()[0]
    updated_user = User(updated_user_data[1], updated_user_data[2], updated_user_data[3], updated_user_data[4])
    updated_user.id = updated_user_data[0]
    
    assert updated_user.name == "Ouango Bénédicte"
    assert updated_user.address == "Bobo"
    assert updated_user.email == "nouveauemail@gmail.com"

# Test de la méthode login
def test_login_valid_infos():
    # Assume you have a test user in the database with valid credentials
    user = User.login("coco@gmail.com", "1234")
    assert user is not None

def test_login_invalid_infos():
    user = User.login("invalid@gmail.com", "mauvais")
    assert user is None


