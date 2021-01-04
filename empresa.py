# Linguagem de Programação II
# Atividade Contínua 04 - Classes abstratas, herança e polimorfismo
# Arquivo: empresa.py
# Prof. Rafael Maximo
#
# e-mail: lucas.tavernari@aluno.faculdadeimpacta.com.br


# Lembre-se de importar as classes que forem necessárias do modulo funcionarios.py

from funcionarios import Vendedor

class Empresa:

    def __init__(self, nome, cnpj, area_atuacao, equipe):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__area_atuacao = area_atuacao
        self.__equipe = equipe

    def contrata(self, novo_funcionario):
        self.__equipe.append(novo_funcionario)

    @property
    def equipe(self):
        return self.__equipe

    def folha_pagamento(self):
        total = 0
        for funcionario in self.__equipe:
            total += funcionario.calcula_salario()
        return total

    def dissidio_anual(self):
        for funcionario in self.__equipe:
            funcionario.aumenta_salario()

    def listar_visitas(self):
        funcionarios = {}
        for funcionario in self.__equipe:
            if isinstance(funcionario, Vendedor):
                funcionarios[funcionario.email] = funcionario.visitas
        return funcionarios

    def zerar_visitas_vendedores(self):
        for funcionario in self.__equipe:
            if isinstance(funcionario, Vendedor):
                funcionario.zerar_visitas()