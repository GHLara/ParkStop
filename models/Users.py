usersgenerate = [["José", "Jose@gmail.com"],
    ["Pedro", "Pedro@gmail.com"],
    ["Mileny", "Mileny@gmail.com"],
    ["Jefferson", "Jeffeson@gmail.com"],
    ["Julia", "Julia@gmail.com"],
    ["Marcos", "Marcos@gmail.com"],
    ["Suzana", "Suzana@gmail.com"]
]

users = []

def Register(nome, usuario, email, senha):
    newUser = User(nome, usuario, email, senha)
    users.append(newUser)

def GetUsers():
    return f'{users[0].nome}'

class User():
    def __init__(self, nome, usuario, email, senha):
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha

admin = User(nome='Administrador', email='Admin@admin', senha='adm123', usuario='Admin')

for user in usersgenerate:
    newUser = User(nome=user[0], email=user[1], senha='teste', usuario='indiferente')
    users.append(newUser)
    
users.append(admin)