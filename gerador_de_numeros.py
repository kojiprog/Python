import random


class Gerador:

    def __init__(self):
        self.minimo = 1
        self.maximo = 6

    def Inicio(self):
        self.Gerador_aliatorio()
        self.Perguntar_novamente()

    def Perguntar_novamente(self):
        self.resposta = input('Deseja rodar novamente?(s/n)')

        if self.resposta == 's':
            self.Inicio()

        elif self.resposta == 'n':

            print('Ok! Obrigado por usar nosso programa')


        else:
            print('Digite \'s\' para SIM ou \'n\' para NÃO')

            self.Perguntar_novamente()

    def Gerador_aliatorio(self):
        print(random.randint(self.minimo, self.maximo))


inicializador = Gerador()
inicializador.Inicio()
