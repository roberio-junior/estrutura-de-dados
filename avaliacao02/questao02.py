from collections import deque  # deque é uma fila eficiente em Python

class FilaLanchonete:
    def __init__(self):
        self.fila = deque()  # cria a fila vazia

    def chegada_cliente(self, cliente):
        self.fila.append(cliente)  # adiciona cliente no final da fila
        print(f"Cliente {cliente} chegou à fila.")

    def atender_cliente(self):
        if not self.fila:
            print("Fila vazia. Nenhum cliente para atender.")
        else:
            atendido = self.fila.popleft()  # remove cliente do início da fila
            print(f"Cliente {atendido} foi atendido.")

    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
        else:
            print("Fila atual:", list(self.fila))


# Função com menu para interagir
def menu_fila():
    fila = FilaLanchonete()

    while True:
        print("\nMenu da fila da lanchonete:")
        print("1 - Adicionar cliente.")
        print("2 - Atender cliente.")
        print("3 - Exibir os clientes que ainda estão na fila.")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente que chegou: ")
            fila.chegada_cliente(nome)
        elif opcao == "2":
            fila.atender_cliente()
        elif opcao == "3":
            fila.mostrar_fila()
        elif opcao == "0":
            print("Encerrando o sistema de fila.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu_fila()
