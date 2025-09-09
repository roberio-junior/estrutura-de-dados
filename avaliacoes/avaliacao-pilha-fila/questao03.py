# Exibe o texto atual juntando as palavras com espaço
def exibir_texto(palavras):
    texto = " ".join(palavras)
    print(f"Texto atual: {texto}")

# Remove a última palavra digitada, se houver
def desfazer(palavras):
    if palavras:
        palavras.pop()
    exibir_texto(palavras)

# Menu principal do programa
def menu():
    palavras = []  # Lista para armazenar as palavras digitadas

    while True:
        print("\n╔══════════════════════════════╗")
        print("║             MENU             ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Digitar                   ║")
        print("║ 2. < Desfazer                ║")
        print("║ 0. x Sair                    ║")
        print("╚══════════════════════════════╝")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            entrada = input("Digite algo: ")
            palavras.extend(entrada.split())  # Adiciona as palavras digitadas à lista
            exibir_texto(palavras)

        elif escolha == "2":
            desfazer(palavras)  # Remove a última palavra

        elif escolha == "0":
            print("Encerrando Editor...")
            break  # Encerra o programa

        else:
            print("Opção inválida. Tente novamente.")

menu()
