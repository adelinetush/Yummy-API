''
'base class for all users'
''
class User:
    def __init__(self, name, email, password):
        self.Id = range(0, 1000, 1)
        self.username = name
        self.email = email;
        self.password = password

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }