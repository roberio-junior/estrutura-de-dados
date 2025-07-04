fila_onibus = []  # Lista que representa a fila de passageiros no ônibus

def embarcar():
    nome = input("Nome do passageiro para embarcar: ")
    fila_onibus.append(nome)  # Adiciona passageiro no final da fila (embarque)
    print(f"{nome} embarcou no ônibus.")

def desembarcar():
    if len(fila_onibus) == 0:  # Verifica se a fila está vazia
        print("Ônibus vazio. Nenhum passageiro para desembarcar.")
    else:
        nome = fila_onibus.pop(0)  # Remove passageiro do início da fila (desembarque)
        print(f"{nome} desembarcou do ônibus.")

def mostrar_passageiros():
    if len(fila_onibus) == 0:
        print("Ônibus vazio.")
    else:
        print("Passageiros no ônibus (ordem de embarque):")
        for i, nome in enumerate(fila_onibus, 1):  # Mostra os passageiros em ordem
            print(f"{i}. {nome}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Embarcar passageiro")
        print("2 - Desembarcar passageiro")
        print("3 - Mostrar passageiros")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            embarcar()
        elif opcao == "2":
            desembarcar()
        elif opcao == "3":
            mostrar_passageiros()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
