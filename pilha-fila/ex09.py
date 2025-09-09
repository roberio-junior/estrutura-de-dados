# Classe que representa uma pilha para armazenar os estados do jogo
class PilhaEstados:
    def __init__(self):
        self.estados = []  # lista usada como pilha para armazenar os estados

    # Salva um novo estado no topo da pilha
    def salvar_estado(self, estado):
        self.estados.append(estado)
        print(f"Estado salvo: {estado}")

    # Volta para o estado anterior, removendo o topo da pilha
    def voltar_estado(self):
        if not self.estados:
            print("Não há estados anteriores para voltar.")
        else:
            removido = self.estados.pop()
            print(f"Voltando do estado: {removido}")

    # Mostra o estado atual (último da pilha)
    def estado_atual(self):
        if not self.estados:
            print("Nenhum estado atual.")
        else:
            print(f"Estado atual: {self.estados[-1]}")

    # Mostra todos os estados salvos até agora
    def mostrar_historico(self):
        if not self.estados:
            print("Histórico vazio.")
        else:
            print("Histórico de estados:", self.estados)


# Função principal que exibe um menu para o usuário interagir
def menu_jogo():
    jogo = PilhaEstados()  # cria uma pilha para armazenar os estados

    while True:
        # Exibe as opções do menu
        print("\nMenu do Jogo:")
        print("1 - Avançar (salvar novo estado)")
        print("2 - Voltar para estado anterior")
        print("3 - Ver estado atual")
        print("4 - Mostrar histórico")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")  # lê a escolha do usuário

        # Executa ações conforme a opção escolhida
        if opcao == "1":
            estado = input("Digite o nome do novo estado (ex: Fase 2, Chefe final): ")
            jogo.salvar_estado(estado)
        elif opcao == "2":
            jogo.voltar_estado()
        elif opcao == "3":
            jogo.estado_atual()
        elif opcao == "4":
            jogo.mostrar_historico()
        elif opcao == "0":
            print("Saindo do jogo...")
            break  # encerra o programa
        else:
            print("Opção inválida. Tente novamente.")  # entrada incorreta

# Inicia o programa chamando o menu
menu_jogo()
