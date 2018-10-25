class Usuario():
    def __init__(self, id, login, senha, dt_expiracao):
        self.id = id
        self.login = login
        self.__senha = senha
        self.dt_expiracao = dt_expiracao
        self.lista_coordenadores = []
        self.lista_alunos = []
    
    def imprime(self):
        return self.__senha

    def imprime_lista(self):
        for alunos in self.lista_alunos:
            print(self.lista_alunos[alunos])
            print(alunos)


user1 = Usuario(10597, 'user1', '123', '28-05-2019')


class Coordenador():
    def __init__(self, id, usuario, nome, email, celular):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.celular = celular
        self.usuario.lista_coordenadores.append(self)

class Aluno():
    def __init__(self, id, usuario, nome, email, celular, RA):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.email = email
        self.celular = celular
        self.ra = RA
        self.foto = None
        self.usuario.lista_alunos.append(self)

aluno1 = Aluno(10597, user1, 'Gabriel', 'gmorais@me.com', '40028922', 1800691)
print(Usuario.imprime_lista)