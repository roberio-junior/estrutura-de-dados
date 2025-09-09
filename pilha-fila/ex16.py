fila_senhas = []      # Lista que guarda as senhas na ordem que foram retiradas
proxima_senha = 1     # Número da próxima senha a ser gerada

def retirar_senha():
    global proxima_senha
    fila_senhas.append(proxima_senha)  # Adiciona a nova senha ao final da fila
    print(f"Senha {proxima_senha} retirada. Aguarde sua vez.")
    proxima_senha += 1  # Incrementa para a próxima senha

def atender_senha():
    if len(fila_senhas) == 0:          # Verifica se não há senhas na fila
        print("Não há senhas para atendimento.")
    else:
        senha_atendida = fila_senhas.pop(0)  # Remove a senha mais antiga da fila
        print(f"Atendendo a senha {senha_atendida}.")
        mostrar_fila()  # Mostra a fila atualizada

def mostrar_fila():
    if len(fila_senhas) == 0:
        print("Fila de espera vazia.")
    else:
        # Exibe as senhas na fila separadas por vírgula
        print("Fila atual de espera: ", end="")
        print(", ".join(str(s) for s in fila_senhas))

def menu():
    while True:
        print("\nMenu:")
        print("1 - Retirar senha")
        print("2 - Atender próxima senha")
        print("3 - Mostrar fila")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            retirar_senha()
        elif opcao == "2":
            atender_senha()
        elif opcao == "3":
            mostrar_fila()
        elif opcao == "0":
            print("Encerrando sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
