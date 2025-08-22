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
            self.fome -= self.fome * (quantidade/100)
            if self.fome < 0:
                self.fome = 0

    def brincar(self, quantidade):
        if 0 <= quantidade <= 100:
            self.tedio -= self.tedio * (quantidade/100)
            if self.tedio < 0:
                self.tedio = 0

    def getHumor(self):
        return max(0, 100 - ((self.fome + self.tedio)/2))

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
            print(f"{self.nome} MORRIII :( ")

    def tempoPassando(self):
        self.vida()
        if self.saude <= 0:
            return
        self.idade += 0.2
        self.tedio += 2.5
        self.fome += 5
        if self.fome > 100:
            self.fome = 100
        if self.tedio > 100:
            self.tedio = 100

    def status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Fome: {round(self.fome,1)}%")
        print(f"Tédio: {round(self.tedio,1)}%")
        print(f"Saúde: {self.saude} ❤")
        print(f"Idade: {round(self.idade,1)} anos\n")


# ============= Classes =================== #
class Kuromi(Tamagoshi):
    def __init__(self, nome="Kuromi"):
        super().__init__(nome)
        self.brava = True
        self.diversao = 100
        self.tipoFome = "amora"

    def aprontar(self):
        print(f"{self.nome} aprontou algo!")
        self.tedio -= 15
        self.diversao += 10

    def gargalhar(self):
        print(f"{self.nome} deu uma risada malvada")
        self.tedio -= 10

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: estou BRAVA! Quero comer já!")
        if self.tedio > 50:
            print(f"{self.nome}: to entediada, vamos aprontar!")


class MyMelody(Tamagoshi):
    def __init__(self, nome="My Melody"):
        super().__init__(nome)
        self.fofa = True
        self.carinho = 50
        self.tipoFome = "docinho"

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
        self.tipoFome = "manga"
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

class HelloKitty(Tamagoshi):
    def __init__(self, nome="Hello Kitty"):
        super().__init__(nome)
        self.amigavel = True
        self.tipoFome = "maçã"

    def abraçar(self):
        print(f"{self.nome} te deu um abraço fofo ❤")
        self.saude += 10
        self.tedio -= 10

    def cantar(self):
        print(f"{self.nome} está cantando uma música alegre")
        self.tedio -= 15

    def reclamar(self):
        if self.fome > 50:
            print(f"{self.nome}: Queria uma maçã agora!")
        if self.tedio > 50:
            print(f"{self.nome}: Estou entediada, vamos cozinharr juntas")


    


# ================== Geladeira =============== #
def abrirGeladeira(animal):
    print("\n--- Geladeira ---")
    comidaEscolhida = ""
    if isinstance(animal, Kuromi):
        print("1 - Carne (40%)")
        print("2 - Cebola em conserva (80%)")
        print("3 - Charlotas (comida favorita 100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1":
            animal.alimentar(40); comidaEscolhida = "Carne"
        elif escolha == "2":
            animal.alimentar(80); comidaEscolhida = "Cebola em conserva"
        elif escolha == "3":
            animal.alimentar(100); comidaEscolhida = "Charlotas"
    elif isinstance(animal, MyMelody):
        print("1 - Suco de pêssego (40%)")
        print("2 - Galette de morango (80%)")
        print("3 - Bolo de amêndoas (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1":
            animal.alimentar(40); comidaEscolhida = "Suco de pêssego"
        elif escolha == "2":
            animal.alimentar(80); comidaEscolhida = "Galette de morango"
        elif escolha == "3":
            animal.alimentar(100); comidaEscolhida = "Bolo de amêndoas"
    elif isinstance(animal, Pompompurin):
        print("1 - Leite (40%)")
        print("2 - Flan (80%)")
        print("3 - Pudim (100%)")
        escolha = input("Escolha a comida: ")
        if escolha == "1":
            animal.alimentar(40); comidaEscolhida = "Leite"
        elif escolha == "2":
            animal.alimentar(80); comidaEscolhida = "Flan"
        elif escolha == "3":
            animal.alimentar(100); comidaEscolhida = "Pudim"
    if comidaEscolhida:
        print(f"{animal.nome} comeu {comidaEscolhida}! ({animal.tipoFome})")
        


# ======================= Main ========================= #
def main():
    print("─── ⋆⋅☆⋅⋆ ──  Bem-vindo ao Tamagotchi Sanrio ─── ⋆⋅☆⋅⋆ ──")
    print("Escolha seu bichinho:")
    print("1 - Kuromi (brava, muita fome, ama se divertir)")
    print("2 - My Melody (fofa, ama carinho e docinhos)")
    print("3 - Pompompurin (dorminhoco, calmo, ama pudim)")
    escolha = input("Digite o número: ")

    if escolha == "1":
        animalzinho = Kuromi()
    elif escolha == "2":
        animalzinho = MyMelody()
    else:
        animalzinho = Pompompurin()

    print(f"\nVocê adotou {animalzinho.nome} ִ ࣪𖤐 ")

    while True:
        if animalzinho.saude <= 0:
            print(f"{animalzinho.nome} morreu :O ---- fim de jogo!")
            break

        print("\nO que deseja fazer?")
        print("1 - Alimentar rápido (50%)")
        print("2 - Brincar")
        print("3 - Ver humor")
        print("4 - Ação especial do bichinho")
        print("5 - ABRIR GELADEIRA")
        print("6 - Sair do jogo")

        acao = input("Escolha: ")

        if acao == "1":
            animalzinho.alimentar(50)
            print(f"{animalzinho.nome} foi alimentado ❤︎ ({animalzinho.tipoFome})")
        elif acao == "2":
            animalzinho.brincar(50)
            print(f"{animalzinho.nome} se divertiu ₍^. .^₎⟆ ")
        elif acao == "3":
            print(f"Humor: {animalzinho.getHumor()}%")
        elif acao == "4":
            if isinstance(animalzinho, Kuromi):
                animalzinho.aprontar()
            elif isinstance(animalzinho, MyMelody):
                animalzinho.receberCarinho()
            elif isinstance(animalzinho, Pompompurin):
                animalzinho.comerPudim()
        elif acao == "5":
            abrirGeladeira(animalzinho)
        elif acao == "6":
            print(f"{animalzinho.nome} foi dormir ... nao acorde")
            break
        else:
            print("Essa opção não existe")

        animalzinho.tempoPassando()
        animalzinho.reclamar()
        animalzinho.status()

if __name__ == "__main__":
    main()
