# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: funcionarios.py
# Prof. Rafael Maximo
#
# e-mail: lucas.tavernari@aluno.faculdadeimpacta.com.br


class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Funcionario(Pessoa):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        Pessoa.__init__(self, nome, idade)
        self.__email = email
        self.__salario_base = 0
        self.__carga_horaria_semanal = carga_horaria_semanal

    def calcula_salario(self):
        return self.carga_horaria * self.salario_base * 4.5

    @property
    def email(self):
        return self.__email

    @property
    def carga_horaria(self):
        return self.__carga_horaria_semanal

    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        self.__carga_horaria_semanal = nova_carga_horaria

    def aumenta_salario(self):
        self.salario_base += self.salario_base * 0.05

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self.__salario_base = salario_base

class Programador(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        Funcionario.__init__(self, nome, idade, email, carga_horaria_semanal)
        self.salario_base = 35
        self.carga_horaria = carga_horaria_semanal

    @Funcionario.carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria >= 20 and nova_carga_horaria <= 40:
            Funcionario.carga_horaria.fset(self, nova_carga_horaria)
        else:
            raise ValueError('A carga horária deve estar entre 20 e 40')

class Estagiario(Funcionario):

    def __init__(self, nome, idade, email, carga_horaria_semanal):
        Funcionario.__init__(self, nome, idade, email, carga_horaria_semanal)
        self.salario_base = 15.50
        self.carga_horaria = carga_horaria_semanal

    def calcula_salario(self):
        return self.carga_horaria * self.salario_base * 4.5 + 250

    @Funcionario.carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria >= 16 and nova_carga_horaria <= 30:
            Funcionario.carga_horaria.fset(self, nova_carga_horaria)
        else:
            raise ValueError('A carga horária deve estar entre 16 e 30')

class Vendedor(Funcionario):
    def __init__(self, nome, idade, email, carga_horaria_semanal):
        Funcionario.__init__(self, nome, idade, email, carga_horaria_semanal)
        self.__visitas = 0
        self.salario_base = 30
        self.carga_horaria = carga_horaria_semanal

    def calcula_salario(self):
        pagamento_visitas = self.__visitas * 30
        return self.carga_horaria * self.salario_base * 4.5 + 350 + pagamento_visitas
        
    @Funcionario.carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria >= 15 and nova_carga_horaria <= 45:
            Funcionario.carga_horaria.fset(self, nova_carga_horaria)
        else:
            raise ValueError('A carga horária deve estar entre 15 e 45')

    @property
    def visitas(self):
        return self.__visitas

    def realizar_visita(self, n_visitas):
        if isinstance(n_visitas, int):
            if n_visitas > 0:
                self.__visitas += n_visitas
            else:
                raise ValueError ("O número deve ser positivo.")
        else:
            raise TypeError ("O número deve ser inteiro.")

    def zerar_visitas(self):
        self.__visitas = 0