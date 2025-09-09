from collections import deque

# Fila global de tarefas
fila_tarefas = deque()

# Adiciona tarefa à fila
def adicionar_tarefa(nome, prioridade):
    prioridades_validas = ["baixa", "média", "media", "alta"]
    if prioridade.lower() not in prioridades_validas:
        print("Prioridade inválida. Insira baixa, média ou alta.")
        return
    tarefa = {"nome": nome, "prioridade": prioridade.lower()}
    fila_tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com prioridade {prioridade}.")

# Executa (remove) a próxima tarefa da fila
def executar_tarefa():
    if not fila_tarefas:
        print("Nenhuma tarefa para executar.")
    else:
        tarefa = fila_tarefas.popleft()
        print(f"Executando tarefa: {tarefa['nome']} (prioridade: {tarefa['prioridade']})")

# Mostra a próxima tarefa da fila sem remover
def mostrar_proxima_tarefa():
    if not fila_tarefas:
        print("Nenhuma tarefa agendada.")
    else:
        tarefa = fila_tarefas[0]
        print(f"Próxima tarefa: {tarefa['nome']} - Prioridade: {tarefa['prioridade']}")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar tarefa")
        print("2 - Executar próxima tarefa")
        print("3 - Mostrar próxima tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            prioridade = input("Prioridade (baixa, média, alta): ")
            adicionar_tarefa(nome, prioridade)
        elif opcao == "2":
            executar_tarefa()
        elif opcao == "3":
            mostrar_proxima_tarefa()
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
