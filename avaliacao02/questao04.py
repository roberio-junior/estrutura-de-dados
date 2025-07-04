from collections import deque  # Importa deque para usar como fila

class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome # Nome da tarefa
        self.prioridade = prioridade  # Nível de prioridade da tarefa

class Gerenciador:
    def __init__(self):
        self.fila_tarefas = deque()  # Fila que armazena as tarefas na ordem de chegada

    def adicionar_tarefa(self, nome, prioridade):
        tarefa = Tarefa(nome, prioridade)  # Cria uma nova tarefa
        self.fila_tarefas.append(tarefa) # Adiciona a tarefa no final da fila
        print(f"Tarefa '{nome}' adicionada com prioridade {prioridade}.")

    def executar_tarefa(self):
        if self.fila_tarefas: # Verifica se há tarefas na fila
            tarefa = self.fila_tarefas.popleft()  # Remove a tarefa mais antiga da fila
            print(f"Executando tarefa: {tarefa.nome} (prioridade: {tarefa.prioridade})")
        else:
            print("Nenhuma tarefa para executar.")

    def mostrar_fila(self):
        if not self.fila_tarefas: # Verifica se a fila está vazia
            print("Nenhuma tarefa agendada.")
        else:
            print("Próxima tarefa:")
            proxima = self.fila_tarefas.popleft()
            # coloca a tarefa no final da fila
            self.fila_tarefas.append(proxima)
            # organiza a fila
            for i in range (len(self.fila_tarefas)-1):
                organiza = self.fila_tarefas.popleft()
                self.fila_tarefas.append(organiza)
            print(f"{proxima.nome} prioridade: {proxima.prioridade}")
def menu():
    gerenciador = Gerenciador() # Cria o gerenciador de tarefas
    while True:
        print("\nMenu:")
        print("1 - Adicionar tarefa.")
        print("2 - Executar próxima tarefa.")
        print("3 - Mostrar próxima.")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            prioridade = input("Prioridade da tarefa (baixa, média ou alta): ")
            prioridades = ["baixa", "média", "alta"]
            if prioridade in prioridades: # Verifica se a prioridade é valida
                gerenciador.adicionar_tarefa(nome, prioridade)
            else:
                print("prioridade inválida. Insira baixa, média ou alta.")
        elif opcao == "2":
            gerenciador.executar_tarefa()
        elif opcao == "3":
            gerenciador.mostrar_fila()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
