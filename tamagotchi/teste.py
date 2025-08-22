# -*- coding: utf-8 -*-
# Mary - Tamagotchi Sanrio

class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.tipoFome = "fome normal"

    def alimentar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.fome -= self.fome * (quantidade / 100)
            if self.fome < 0:
                self.fome = 0

    def brincar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.tedio -= self.tedio * (quantidade / 100)
            if self.tedio < 0:
                self.tedio = 0

    def getHumor(self):
        return max(0, 100 - ((self.fome + self.tedio) / 2))

    def vida(self):
        if self.saude <= 0:
            return
        if (50 < self.fome <= 60) or (50 < self.tedio <= 60):
            self.saude -= 10
        elif (60 < self.fome <= 80) or (60 < self.tedio <= 80):
            self.saude -= 30
        elif (80 < self.fome <= 90) or (80 < self.tedio <= 90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70
            print(f"{self.nome}: Estou morrendo... (irresponsável)")
        if 0 < self.saude <= 30:
            print(f"ALERTA: {self.nome} está muito fraco! Cuida logo dele!")
        if self.saude <= 0:
            self.saude = 0
            print(f"{self.nome} MORRIII :(")

    def tempoPassando(self):
        self.vida()
        if self.saude <= 0:
            return
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        self.fome = min(self.fome, 100)
        self.tedio = min(max(self.tedio, 0), 100)  

    def status(self):
        print("\n" + "-"*30)
        print(f"Status de {self.nome}:")
        print(f"Fome: {round(self.fome,1)}%")
        print(f"Tédio: {round(self.tedio,1)}%")
        print(f"Saúde: {self.saude}")
        print(f"Idade: {round(self.idade,1)} anos")
        print("-"*30 + "\n")

    def acaoEspecial(self):
        print(f"{self.nome} não tem ação especial :(")

    def abrirGeladeira(self):
        print(f"{self.nome} não tem geladeira :(")


# ================= Classes =================== #
class Kuromi(Tamagoshi):
    def __init__(self, nome="Kuromi"):
        super().__init__(nome)
        self.diversao = 100
        self.tipoFome = "amora"

    def aprontar(self):
        print(f"{self.nome} aprontou algo!")
        self.tedio = max(0, self.tedio - 15)
        self.diversao += 10

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: estou BRAVA! Quero comer já!")
        if self.tedio > 50:
            print(f"{self.nome}: to entediada, vamos aprontar!")

    def acaoEspecial(self):
        self.aprontar()

    def abrirGeladeira(self):
        print("\n--- Geladeira de Kuromi ---")
        print("1 - Carne (40%)\n2 - Cebola em conserva (80%)\n3 - Charlotas (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1": 
            self.alimentar(40)
            comida = "Carne"
        elif escolha == "2": 
            self.alimentar(80)
            comida = "Cebola em conserva"
        elif escolha == "3": 
            self.alimentar(100)
            comida = "Charlotas"
        else:
            comida = "nada"
            print("Opção inválida!")
        print(f"{self.nome} comeu {comida}! ({self.tipoFome})\n")


class MyMelody(Tamagoshi):
    def __init__(self, nome="My Melody"):
        super().__init__(nome)
        self.carinho = 50
        self.tipoFome = "docinho"

    def receberCarinho(self):
        print(f"{self.nome} adorou o carinho :)")
        self.carinho += 20
        self.tedio = max(0, self.tedio - 10)

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Queria um docinho agora ")
        if self.tedio > 50:
            print(f"{self.nome}: Me dá carinho, por favor ")

    def acaoEspecial(self):
        self.receberCarinho()

    def abrirGeladeira(self):
        print("\n--- Geladeira de My Melody ---")
        print("1 - Suco de pêssego (40%)\n2 - Galette de morango (80%)\n3 - Bolo de amêndoas (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1": 
            self.alimentar(40)
            comida = "Suco de pêssego"
        elif escolha == "2": 
            self.alimentar(80)
            comida = "Galette de morango"
        elif escolha == "3": 
            self.alimentar(100)
            comida = "Bolo de amêndoas"
        else:
            comida = "nada"
            print("Opção inválida!")
        print(f"{self.nome} comeu {comida}! ({self.tipoFome})\n")


class Pompompurin(Tamagoshi):
    def __init__(self, nome="Pompompurin"):
        super().__init__(nome)
        self.tipoFome = "manga"

    def comerPudim(self):
        print(f"{self.nome} comeu um pudim delicioso!")
        self.alimentar(20)

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Quero pudimmmm :D")
        if self.tedio > 50:
            print(f"{self.nome}: Tô entediado... mas queria dormir ")

    def acaoEspecial(self):
        self.comerPudim()

    def abrirGeladeira(self):
        print("\n--- Geladeira de Pompompurin ---")
        print("1 - Leite (40%)\n2 - Flan (80%)\n3 - Pudim (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1": 
            self.alimentar(40)
            comida = "Leite"
        elif escolha == "2": 
            self.alimentar(80)
            comida = "Flan"
        elif escolha == "3": 
            self.alimentar(100)
            comida = "Pudim"
        else:
            comida = "nada"
            print("Opção inválida!")
        print(f"{self.nome} comeu {comida}! ({self.tipoFome})\n")


class HelloKitty(Tamagoshi):
    def __init__(self, nome="Hello Kitty"):
        super().__init__(nome)
        self.tipoFome = "maçã"

    def cozinhar(self):
        print(f"{self.nome} está cozinhando uma receita deliciosa!")
        self.tedio = max(0, self.tedio - 15)

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Queria uma maçã agora!")
        if self.tedio > 50:
            print(f"{self.nome}: Estou entediada, vamos cozinhar juntas!")

    def acaoEspecial(self):
        self.cozinhar()

    def abrirGeladeira(self):
        print("\n--- Geladeira de Hello Kitty ---")
        print("1 - Maçã (40%)\n2 - Bolo de cenoura (80%)\n3 - Cupcake (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1": 
            self.alimentar(40)
            comida = "Maçã"
        elif escolha == "2": 
            self.alimentar(80)
            comida = "Bolo de cenoura"
        elif escolha == "3": 
            self.alimentar(100)
            comida = "Cupcake"
        else:
            comida = "nada"
            print("Opção inválida!")
        print(f"{self.nome} comeu {comida}! ({self.tipoFome})\n")


class Chocoket(Tamagoshi):
    def __init__(self, nome="Chocoket"):
        super().__init__(nome)
        self.tipoFome = "chocolate"

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Quero chocolate agora!")
        if self.tedio > 50:
            print(f"{self.nome}: Estou entediado!")

    def abrirGeladeira(self):
        print(f"{self.nome} não tem geladeira :(\n")


class Cinnamoroll(Tamagoshi):
    def __init__(self, nome="Cinnamoroll"):
        super().__init__(nome)
        self.tipoFome = "rolinhos de canela"

    def voar(self):
        print(f"{self.nome} está voando pelo céu!")
        self.tedio = max(0, self.tedio - 20)

    def receberCarinho(self):
        print(f"{self.nome} adorou o carinho :3")
        self.tedio = max(0, self.tedio - 10)

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Quero rolinhos de canela agora!")
        if self.tedio > 50:
            print(f"{self.nome}: Estou entediado... vamos brincar!")

    def acaoEspecial(self):
        self.voar()

    def abrirGeladeira(self):
        print(f"{self.nome} não tem geladeira :(\n")


# ================= Main =================== #
def main():
    print("-"*97)
    print("Bem-vindo ao Tamagotchi Sanrio")
    print("-"*97 + "\n")

    print("Escolha seu bichinho:")
    print("1 - Kuromi\n2 - My Melody\n3 - Pompompurin\n4 - Hello Kitty\n5 - Chocoket\n6 - Cinnamoroll")
    escolha = input("Digite o número: ")

    if escolha == "1": animalzinho = Kuromi()
    elif escolha == "2": animalzinho = MyMelody()
    elif escolha == "3": animalzinho = Pompompurin()
    elif escolha == "4": animalzinho = HelloKitty()
    elif escolha == "5": animalzinho = Chocoket()
    elif escolha == "6": animalzinho = Cinnamoroll()
    else:
        print("Esse não existe, adotando Kuromi por padrão")
        animalzinho = Kuromi()

    print(f"\nVocê adotou {animalzinho.nome}\n")

    while True:
        if animalzinho.saude <= 0:
            print(f"{animalzinho.nome} morreu ---- fim de jogo!")
            break

        print("\nO que deseja fazer?")
        print("1 - Alimentar rápido (50%)")
        print("2 - Brincar")
        print("3 - Ver humor")
        print("4 - Ação especial do bichinho")
        print("5 - ABRIR GELADEIRA")
        print("6 - Sair do jogo")
        print("-"*30)

        acao = input("Escolha: ")

        if acao == "1":
            animalzinho.alimentar(50)
            print(f"{animalzinho.nome} foi alimentado ({animalzinho.tipoFome})\n")
        elif acao == "2":
            animalzinho.brincar(50)
            print(f"{animalzinho.nome} se divertiu\n")
        elif acao == "3":
            print(f"Humor: {animalzinho.getHumor()}%\n")
        elif acao == "4":
            animalzinho.acaoEspecial()
        elif acao == "5":
            animalzinho.abrirGeladeira()
        elif acao == "6":
            print(f"{animalzinho.nome} foi dormir ... não acorde\n")
            break
        else:
            print("Essa opção não existe\n")

        animalzinho.tempoPassando()
        animalzinho.reclamar()
        animalzinho.status()


if __name__ == "__main__":
    main()
