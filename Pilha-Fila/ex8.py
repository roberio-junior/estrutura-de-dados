# Classe Pilha com capacidade limitada
class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade  # define o tamanho máximo da pilha
        self.itens = []               # lista que armazena os elementos da pilha

    def esta_vazia(self):
        return len(self.itens) == 0  # retorna True se a pilha estiver vazia

    def esta_cheia(self):
        return len(self.itens) == self.capacidade  # retorna True se estiver cheia

    def empilhar(self, item):
        if self.esta_cheia():
            print("Erro: pilha cheia. Não é possível empilhar.")
        else:
            self.itens.append(item)  # adiciona item ao topo da pilha
            print(f"{item} empilhado.")

    def desempilhar(self):
        if self.esta_vazia():
            print("Erro: pilha vazia. Não é possível desempilhar.")
        else:
            removido = self.itens.pop()  # remove o item do topo
            print(f"{removido} desempilhado.")

    def mostrar(self):
        if self.esta_vazia():
            print("Pilha vazia.")
        else:
            print("Pilha atual:", self.itens)  # mostra todos os elementos


# Função com menu interativo
def menu_pilha():
    # Solicita ao usuário a capacidade da pilha
    capacidade = int(input("Defina a capacidade da pilha: "))
    pilha = Pilha(capacidade)  # cria a pilha com essa capacidade

    while True:
        # Exibe as opções disponíveis
        print("\nMenu:")
        print("1 - Empilhar")
        print("2 - Desempilhar")
        print("3 - Mostrar pilha")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Informe o valor a empilhar: ")
            pilha.empilhar(item)
        elif opcao == "2":
            pilha.desempilhar()
        elif opcao == "3":
            pilha.mostrar()
        elif opcao == "0":
            print("Encerrando programa...")
            break  # encerra o loop e o programa
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu_pilha()
