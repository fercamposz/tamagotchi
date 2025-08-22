
from classeMae import Tamagoshi

class Kuromi(Tamagoshi):
    def __init__(self):
        super().__init__("kuromi")
        self.diversao = 100
        self.tipoFome = "parabens"
        print("Personalidade: Atrevida e bagunceira")

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
        print("\n--- Geladeira da Kuromi ---")
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
    def __init__(self):
        super().__init__("My Melody")
        self.carinho = 50
        self.tipoFome = "arrasouu"
        print("Personalidade: Doce, honesta e atenciosa ")

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
        print("\n--- Geladeira da My Melody ---")
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
    def __init__(self):
        super().__init__("Pompompurin")
        self.tipoFome = "estou feliz por comer"
        print("Personalidade: Preguiçoso e relaxado ")

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
    def __init__(self):
        super().__init__("Hello Kitty")
        self.tipoFome = "hummmmmmm"
        print("Personalidade: Alegre e gentil")

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
        print("\n--- Geladeira da Hello Kitty ---")
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
    def __init__(self):
        super().__init__("Chocoket")
        self.tipoFome = "nhami nham"
        print("Personalidade: Curioso e Inteligente")

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Quero chocolate agora!")
        if self.tedio > 50:
            print(f"{self.nome}: Estou entediado!")

    def abrirGeladeira(self):
        print(f"{self.nome} não tem geladeira :(\n")


class Cinnamoroll(Tamagoshi):
    def __init__(self):
        super().__init__("Cinnamoroll")
        self.tipoFome = ": )"
        print("Personalidade: Timido e fofo")

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