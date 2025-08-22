from classeFilha import *
from classeMae import  *

def main():
    print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･"*5)
    print("\n𝐁𝐞𝐦-𝐯𝐢𝐧𝐝𝐨 𝐚𝐨 𝐓𝐚𝐦𝐚𝐠𝐨𝐭𝐜𝐡𝐢 𝐒𝐚𝐧𝐫𝐢𝐨\n")
    print("°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･"*5 + "\n")


    jogador = input("Digite seu nome: ")


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
