palavras = []

def desfazer():
    global palavras
    palavras.pop()

    texto = ""
    for i in palavras:
        if i == (len(palavras) - 1):
            texto += i
        else:
            texto += i
            texto += " "

    return print(f"Texto atual: {texto}")

def menu():
    global palavras
    texto = ""
    while True:
        print("\n╔══════════════════════════════╗")
        print("║       MENU                   ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Escrever uma palavra      ║")
        print("║ 2. < Desfazer                ║")
        print("║ 0. x Sair                    ║")
        print("╚══════════════════════════════╝")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            palavra = input('Escreva uma palavra:')
            palavras.append(palavra)

            texto = ""
            for i in palavras:
                if i == (len(palavras) - 1):
                    texto += i
            else:
                texto += i
                texto += " "
            print(f"Texto atual: {texto}")

        elif escolha == "2":
            if palavras:
                desfazer()

        elif escolha == "0":
            print("Encerrando Editor...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()