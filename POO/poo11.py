# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        conection = cls()
        conection.user = user
        conection.password = password
        return conection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)


#c1 = Connection()

#c1.set_user('thiago207')
#c1.set_password('F12l?')
#print(c1.user, c1.host, c1.password)

c1 = Connection.create_with_auth('thiago207', 'F12l?')

print(c1.host, c1.user, c1.password)

Connection.log('Bem vindo')