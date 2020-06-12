import time
import random
class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Sim! com certeza",
            "Acho que não",
            "Você é burro é?",
            "Talvez isso possa dar certo",
            "Você tem certeza que quer fazer isso:?",
            "Que tal fazer algo diferente",
            "Acho que alguem já fez isso antes",
            "Eu estava pensando a mesma coisa",
            "Não faço ideia",
            "Péssima ideia",
            "ótima ideia"

        ]

    def Iniciar(self):
        self.FazerPergunta()

    def FazerPergunta(self):
        pergunta = input("Qual é sua duvida?")
        print("pensando...")
        time.sleep(5)
        print(random.choices(self.respostas))
        fazer_outra_pergunta = input("Gostaria de fazer outra pergunta?(s/n)")
        if fazer_outra_pergunta == "s":
            self.FazerPergunta()

        elif fazer_outra_pergunta == "n":
            print("Obrigado por usar nosso programa!")
        else:
            print("Por favor, digite apenas 's' para SIM ou 'n' para NÃO")
            self.Iniciar()


chamar_programa = DecidaPorMim()
chamar_programa.Iniciar()
