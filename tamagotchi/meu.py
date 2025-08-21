# -*- coding: utf-8 -*-  
# Mary Tamagotchi Sanrio 🎀


class Tamagoshi:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0
        self.tedio = 0
        self.tipoFome = "fome normal"

    def alimentar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade/100)
            if self.fome < 0:
                self.fome = 0

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.tedio -= self.tedio * (quantidade/100)
            if self.tedio < 0:
                self.tedio = 0

    def getHumor(self):
        return max(0, 100 - ((self.fome + self.tedio)/2))

    def vida(self):
        if (self.fome > 50 and self.fome <= 60) or (self.tedio > 50 and self.tedio <=60):
            self.saude -= 10
        elif (self.fome > 60 and self.fome <= 80) or (self.tedio > 60 and self.tedio <=80):
            self.saude -= 30
        elif (self.fome > 80 and self.fome <= 90) or (self.tedio > 80 and self.tedio <=90):
            self.saude -= 50
        elif (self.fome > 90) or (self.tedio > 90):
            self.saude -= 70   
            print(f"{self.nome}: Estou morrendo... (irresponsável)")
        elif (self.fome > 99) or (self.tedio > 99):
            self.saude = 0   
            print(f"{self.nome} MORRIII :(")

    def tempoPassando(self):
        self.vida()
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5


# =============== 1 =========== #
class Kuromi(Tamagoshi):
    def __init__(self, nome="Kuromi"):
        super().__init__(nome)
        self.brava = True
        self.diversao = 100
        self.tipoFome = "muita fome"

    def aprontar(self):
        print(f"{self.nome} aprontou algo ")
        self.tedio -= 15
        self.diversao += 10

    def gargalhar(self):
        print(f"{self.nome} deu uma risada malvada")
        self.tedio -= 10

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Estou BRAVA! Quero comer já! ")
        if self.tedio > 50:
            print(f"{self.nome}: Tô entediada, vamos aprontar")


class MyMelody(Tamagoshi):
    def __init__(self, nome="My Melody"):
        super().__init__(nome)
        self.fofa = True
        self.carinho = 50
        self.tipoFome = "fome de docinho"

    def receberCarinho(self):
        print(f"{self.nome} adorou o carinho :)")
        self.carinho += 20
        self.tedio -= 10

    def abraçar(self):
        print(f"{self.nome} te deu um abraço ")
        self.saude += 5

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Queria um docinho agora ")
        if self.tedio > 50:
            print(f"{self.nome}: Me dá carinho, por favor ")


class Pompompurin(Tamagoshi):
    def __init__(self, nome="Pompompurin"):
        super().__init__(nome)
        self.dorminhoco = True
        self.tipoFome = "fome de pudim"
        self.sono = 100

    def dormir(self):
        print(f"{self.nome} está dormindo zzzzzz....")
        self.sono += 20
        self.tedio -= 10

    def sonhar(self):
        print(f"{self.nome} está sonhando com pudim ")
        self.fome += 5

    def comerPudim(self):
        print(f"{self.nome} comeu um pudim mtmt bom")
        self.fome -= 20
        if self.fome < 0:
            self.fome = 0

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Quero pudimmmm :D")
        if self.tedio > 50:
            print(f"{self.nome}: Tô entediado... mas queria dormir ")


# =================2 e 3 desafio =========== #
def main():
    print("─── ⋆⋅☆⋅⋆ ──  Bem-vindo ao Tamagotchi Sanrio ─── ⋆⋅☆⋅⋆ ──")

    print("Escolha seu bichinho:")
    print("1 - Kuromi (brava, muita fome, ama se divertir)")
    print("2 - My Melody (fofa, ama carinho e docinhos)")
    print("3 - Pompompurin (dorminhoco, calmo, ama pudim)")
    escolha = input("Digite o número: ")

    if escolha == "1":
        bicho = Kuromi()
    elif escolha == "2":
        bicho = MyMelody()
    else:
        bicho = Pompompurin()

    print(f"\nVocê adotou {bicho.nome} ִ ࣪𖤐 ")

    while True:
        print("\nO que deseja fazer?")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Ver humor")
        print("4 - Ação especial do bichinho")
        print("5 - Sair do jogo")

        acao = input("Escolha: ")

        if acao == "1":
            bicho.alimentar(50)
            print(f"{bicho.nome} foi alimentado ❤︎ ({bicho.tipoFome})")
        elif acao == "2":
            bicho.brincar(50)
            print(f"{bicho.nome} se divertiu ₍^. .^₎⟆ ")
        elif acao == "3":
            print(f"Humor de {bicho.nome}: {bicho.getHumor()}% ")
            print(f"Saúde: {bicho.saude} ❤︎ | Idade: {round(bicho.idade,1)}")
        elif acao == "4":
            if isinstance(bicho, Kuromi):
                bicho.aprontar()
            elif isinstance(bicho, MyMelody):
                bicho.receberCarinho()
            elif isinstance(bicho, Pompompurin):
                bicho.comerPudim()
        elif acao == "5":
            print(f"{bicho.nome} foi dormir ... nao acorde")
            break
        else:
            print("essa opção nao existe")

        bicho.tempoPassando()
        bicho.reclamar()


if __name__ == "__main__":
    main()
