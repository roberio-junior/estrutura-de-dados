fila = []  # Lista que representa a fila de arquivos para impressão

def enviar_arquivo():
    # Lê nome e quantidade de páginas do arquivo e adiciona na fila
    nome = input("Nome do arquivo: ")
    paginas = input("Quantidade de páginas: ")
    fila.append((nome, paginas))  # Adiciona arquivo (nome, paginas) no final da fila
    print(f"Arquivo '{nome}' com {paginas} páginas adicionado à fila.")

def processar_arquivo():
    # Verifica se a fila está vazia antes de imprimir
    if len(fila) == 0:
        print("Fila vazia. Nenhum arquivo para imprimir.")
    else:
        # Remove o primeiro arquivo da fila para imprimir
        nome, paginas = fila.pop(0)
        print(f"Imprimindo '{nome}' com {paginas} páginas...")
        print(f"Arquivo '{nome}' impresso com sucesso.")

def mostrar_fila():
    # Mostra todos os arquivos que estão na fila
    if len(fila) == 0:
        print("Fila vazia.")
    else:
        print("Fila atual:")
        for i, (nome, paginas) in enumerate(fila, 1):
            print(f"{i}. {nome} ({paginas} páginas)")

def menu():
    # Menu interativo que permite o usuário escolher ações
    while True:
        print("\nMenu:")
        print("1 - Enviar arquivo para impressão")
        print("2 - Processar próximo arquivo")
        print("3 - Mostrar fila")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enviar_arquivo()
        elif opcao == "2":
            processar_arquivo()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "0":
            print("Saindo...")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")

menu()  # Inicia o programa chamando o menu
