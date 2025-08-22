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
            fome_antiga = self.fome
            saude_antiga = self.saude

            self.fome -= self.fome * (quantidade / 100)
            if self.fome < 0:
                self.fome = 0

            self.saude += quantidade * 0.5
            if self.saude > 100:
                self.saude = 100

            self.tedio -= self.tedio * (quantidade / 100)
            if self.tedio < 0:
                self.tedio = 0
   
            reduziu_fome = fome_antiga - self.fome
            recuperou_saude = self.saude - saude_antiga

            print(f"{self.nome} comeu {quantidade}% da comida ({self.tipoFome})")
            print(f"Fome reduzida em {round(reduziu_fome,1)} pontos.")
            print(f"Saúde recuperada em {round(recuperou_saude,1)} pontos!\n")

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
        print(f"Fome: {round(self.fome,1)}")
        print(f"Tédio: {round(self.tedio,1)}")
        print(f"Saúde: {self.saude}")
        print(f"Idade: {round(self.idade,1)} anos")
        print("-"*30 + "\n")

    def acaoEspecial(self):
        print(f"{self.nome} não tem ação especial :(")

    def abrirGeladeira(self):
        print(f"{self.nome} não tem geladeira :(")
