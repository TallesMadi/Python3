# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        # setter
        self.user = user

    def set_password(self, password):
        self.password = password

    def get_user(self):
        # getter
        return self.user

    def get_password(self):
        return self.password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        return f'LOG: {msg}'

c1 = Connection()
c2 = Connection.create_with_auth('Raquel', '123456')

print(c2.get_user())
print(c2.get_password())

print(c1.get_user())
print(c1.get_password())
c1.set_user('Talles')
c1.set_password('a1b2c3')
print(c1.get_user())
print(c1.get_password())

print(c1.log('Pokemon'))