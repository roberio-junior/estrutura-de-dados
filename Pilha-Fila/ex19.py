from collections import deque  # Importa deque para usar como fila

class Tarefa:
    def __init__(self, nome, tempo_estimado):
        self.nome = nome                      # Nome da tarefa
        self.tempo_estimado = tempo_estimado  # Tempo estimado para executar a tarefa

class Agendador:
    def __init__(self):
        self.fila_tarefas = deque()  # Fila que armazena as tarefas na ordem de chegada

    def adicionar_tarefa(self, nome, tempo_estimado):
        tarefa = Tarefa(nome, tempo_estimado)  # Cria uma nova tarefa
        self.fila_tarefas.append(tarefa)       # Adiciona a tarefa no final da fila
        print(f"Tarefa '{nome}' adicionada com tempo estimado de {tempo_estimado} minutos.")

    def executar_tarefa(self):
        if self.fila_tarefas:                  # Verifica se há tarefas na fila
            tarefa = self.fila_tarefas.popleft()  # Remove a tarefa mais antiga da fila
            print(f"Executando tarefa: {tarefa.nome} (Tempo estimado: {tarefa.tempo_estimado} min)")
        else:
            print("Nenhuma tarefa para executar.")

    def mostrar_fila(self):
        if not self.fila_tarefas:              # Verifica se a fila está vazia
            print("Nenhuma tarefa agendada.")
        else:
            print("Fila de tarefas:")
            for i, tarefa in enumerate(self.fila_tarefas, 1):
                # Mostra as tarefas na fila com seu nome e tempo estimado
                print(f"{i}. {tarefa.nome} - {tarefa.tempo_estimado} min")

def menu():
    agendador = Agendador()                   # Cria o agendador de tarefas
    while True:
        print("\nMenu:")
        print("1 - Adicionar tarefa")
        print("2 - Executar próxima tarefa")
        print("3 - Mostrar fila de tarefas")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            tempo = input("Tempo estimado (minutos): ")
            if tempo.isdigit():               # Verifica se tempo é número inteiro
                agendador.adicionar_tarefa(nome, int(tempo))
            else:
                print("Tempo inválido. Insira um número inteiro.")
        elif opcao == "2":
            agendador.executar_tarefa()
        elif opcao == "3":
            agendador.mostrar_fila()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
