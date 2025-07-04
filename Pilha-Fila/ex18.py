from collections import deque  # Importa deque para usar como fila

class Chat:
    def __init__(self):
        self.fila_mensagens = deque()  # Fila que guarda as mensagens na ordem que chegam

    def receber_mensagem(self, mensagem):
        self.fila_mensagens.append(mensagem)  # Adiciona mensagem no final da fila
        print(f"Mensagem recebida: {mensagem}")

    def exibir_mensagens(self):
        if not self.fila_mensagens:
            print("Nenhuma mensagem para exibir.")
        else:
            print("Mensagens no chat:")
            for i, msg in enumerate(self.fila_mensagens, 1):
                print(f"{i}: {msg}")  # Mostra cada mensagem com sua posição

    def remover_mensagem(self):
        if self.fila_mensagens:
            msg = self.fila_mensagens.popleft()  # Remove a mensagem mais antiga (início da fila)
            print(f"Mensagem removida: {msg}")
        else:
            print("Não há mensagens para remover.")

def menu():
    chat = Chat()
    while True:
        print("\nMenu:")
        print("1 - Receber nova mensagem")
        print("2 - Exibir todas as mensagens")
        print("3 - Remover mensagem mais antiga")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            msg = input("Digite a mensagem: ")
            chat.receber_mensagem(msg)
        elif opcao == '2':
            chat.exibir_mensagens()
        elif opcao == '3':
            chat.remover_mensagem()
        elif opcao == '0':
            print("Encerrando o chat.")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
