from collections import deque

def atendimento_fila(clientes):
    fila = deque(clientes)  # Cria uma fila com os clientes na ordem de chegada
    print("Atendimento por fila (FIFO):")
    while fila:
        cliente = fila.popleft()  # Remove o cliente que está na frente da fila (o mais antigo)
        print(f"Atendendo: {cliente}")
    print("Todos os clientes foram atendidos pela fila.\n")

def atendimento_pilha(clientes):
    pilha = list(clientes)  # Cria uma pilha com os clientes (lista)
    print("Atendimento por pilha (LIFO):")
    while pilha:
        cliente = pilha.pop()  # Remove o cliente que chegou por último (topo da pilha)
        print(f"Atendendo: {cliente}")
    print("Todos os clientes foram atendidos pela pilha.\n")

def main():
    clientes = ["Cliente1", "Cliente2", "Cliente3", "Cliente4", "Cliente5"]  # Lista de clientes na ordem de chegada

    print("Clientes na ordem de chegada:", clientes, "\n")

    atendimento_fila(clientes)  # Atendimento FIFO
    atendimento_pilha(clientes)  # Atendimento LIFO

main()
