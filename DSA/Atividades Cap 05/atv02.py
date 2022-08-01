# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():

    def __init__(self, name, city, phone, endereco_email):
        self.nome = name
        self.cidade = city
        self.telefone = phone
        self.email = endereco_email

    def altera_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def altera_cidade(self, nova_cidade):
        self.cidade = nova_cidade

    def print_pessoa(self):
        print(self.nome, self.cidade, self.telefone, self.email)


pessoa = Pessoa('Lucas', 'Campos', '123123', 'lucas@gmail.com')

pessoa.print_pessoa()

pessoa.altera_telefone('456456')

pessoa.print_pessoa()

pessoa.altera_cidade('São joão da barra')

pessoa.print_pessoa()


