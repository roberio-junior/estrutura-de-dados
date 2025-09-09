fila_requisicoes = []  # Lista que guarda as requisições na ordem que chegam

def adicionar_requisicao():
    req = input("ID da requisição para adicionar: ")
    fila_requisicoes.append(req)  # Adiciona nova requisição no final da fila
    print(f"Requisição '{req}' adicionada à fila.")

def processar_requisicao():
    if len(fila_requisicoes) == 0:  # Verifica se a fila está vazia
        print("Nenhuma requisição para processar.")
    else:
        req = fila_requisicoes.pop(0)  # Remove e pega a requisição mais antiga (início da fila)
        print(f"Processando requisição '{req}'... Processada com sucesso.")

def mostrar_fila():
    if len(fila_requisicoes) == 0:
        print("Fila de requisições vazia.")
    else:
        print("Fila atual de requisições:")
        for i, req in enumerate(fila_requisicoes, 1):  # Mostra as requisições com número
            print(f"{i}. {req}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar requisição")
        print("2 - Processar requisição")
        print("3 - Mostrar fila")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_requisicao()
        elif opcao == "2":
            processar_requisicao()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "0":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
