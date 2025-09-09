class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho  # cria lista fixa para guardar os elementos
        self.inicio = 0  # índice do primeiro elemento (mais antigo)
        self.fim = 0     # índice para inserir o próximo elemento
        self.qtd = 0     # quantidade atual de elementos na fila

    def esta_cheia(self):
        return self.qtd == self.tamanho  # retorna True se a fila estiver cheia

    def esta_vazia(self):
        return self.qtd == 0  # retorna True se a fila estiver vazia

    def inserir(self, valor):
        if self.esta_cheia():
            print("Fila cheia! Não é possível inserir.")
            return
        self.fila[self.fim] = valor  # coloca o valor na posição 'fim'
        self.fim = (self.fim + 1) % self.tamanho  # atualiza 'fim' circularmente
        self.qtd += 1  # aumenta a contagem de elementos
        print(f"Elemento '{valor}' inserido na fila.")

    def remover(self):
        if self.esta_vazia():
            print("Fila vazia! Não há elementos para remover.")
            return
        valor = self.fila[self.inicio]  # pega o elemento no início da fila
        self.fila[self.inicio] = None   # limpa a posição (opcional)
        self.inicio = (self.inicio + 1) % self.tamanho  # atualiza 'inicio' circularmente
        self.qtd -= 1  # diminui a contagem de elementos
        print(f"Elemento '{valor}' removido da fila.")

    def mostrar(self):
        if self.esta_vazia():
            print("Fila vazia.")
            return
        print("Fila atual:", end=" ")
        i = self.inicio
        for _ in range(self.qtd):
            print(self.fila[i], end=" ")
            i = (i + 1) % self.tamanho  # avança circularmente na fila
        print()

def menu():
    tamanho = int(input("Defina o tamanho da fila circular: "))
    fila = FilaCircular(tamanho)

    while True:
        print("\nMenu:")
        print("1 - Inserir elemento")
        print("2 - Remover elemento")
        print("3 - Mostrar fila")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = input("Valor a inserir: ")
            fila.inserir(valor)
        elif opcao == "2":
            fila.remover()
        elif opcao == "3":
            fila.mostrar()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
