# users.py
users = []  # Liste vide pour stocker les utilisateurs

class User:
    def __init__(self, name, address, email, password):
        self.id = None
        self.name = name
        self.address = address
        self.email = email
        self.password = password

    @staticmethod
    def create_user(name, address, email, password):
        new_user = User(name, address, email, password)
        new_user.id = len(users) + 1  # ID automatique
        users.append(new_user)
        return new_user
