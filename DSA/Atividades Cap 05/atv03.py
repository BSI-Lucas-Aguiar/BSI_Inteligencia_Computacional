# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone(object):
    def __init__(self, tamanho1, interface1):
        self.tamanho = tamanho1
        self.interface = interface1


class MP3Player(Smartphone):
    def __init__(self, capacidade1, tamanho1, interface1):
        self.capacidade = capacidade1
        self.tamanho = tamanho1
        self.interface = interface1
        Smartphone(tamanho1, interface1)

    def print_mp3(self):
        print(self.capacidade, self.tamanho, self.interface)


mp3 = MP3Player('120Gb', 'Pequeno', 'Led')

mp3.print_mp3()
