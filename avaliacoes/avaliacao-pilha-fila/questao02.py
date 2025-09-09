from collections import deque  # Importa a estrutura deque para representar a fila

# Criamos a fila como uma variável global
fila = deque()

# Adiciona cliente ao final da fila
def chegada_cliente(cliente):
    fila.append(cliente)
    print(f"Cliente {cliente} chegou à fila.")

# Remove o primeiro cliente da fila
def atender_cliente():
    if not fila:
        print("Fila vazia. Nenhum cliente para atender.")
    else:
        atendido = fila.popleft()
        print(f"Cliente {atendido} foi atendido.")

# Exibe todos os clientes que ainda estão na fila
def mostrar_fila():
    if not fila:
        print("A fila está vazia.")
    else:
        print("Fila atual:", list(fila))

# Menu de interação com o usuário
def menu_fila():
    while True:
        print("\nMenu da fila da lanchonete:")
        print("1 - Adicionar cliente.")
        print("2 - Atender cliente.")
        print("3 - Exibir os clientes que ainda estão na fila.")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente que chegou: ")
            chegada_cliente(nome)
        elif opcao == "2":
            atender_cliente()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "0":
            print("Encerrando o sistema de fila.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu_fila()
