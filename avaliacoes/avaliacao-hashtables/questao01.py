def menu():
    contatos = {}
    while True:
        print("\nGerenciador de contatos")
        print("ADD - insere ou atualiza o contato.")
        print("DEL - remove o contato, se existir.")
        print("TEL - imprime o telefone associado ou a mensagem Contato inexistente")
        print("LIST - exibe todos os pares")
        print("SAIR - Sair")

        opcao = input("Escolha uma opção: ")
        opcao = opcao.lower()

        if opcao == "add":
            nome = input("Nome do Contato:")
            numero = int(input("Número do contato:"))
            contatos[numero] = nome

        elif opcao == "dell":
            key = int(input("Número para deletar:"))
            if contatos[key]:
                del contatos[key]
        
        elif opcao == "tell":
            nome = input("Nome do contato:")
            aux = 0
            for key, value in contatos.items():
                if value == nome:
                    print(key)
                    aux += 1
            if aux == 0:
                print("Contato inexistente.")

        
        elif opcao == "list":
            for key, value in contatos.items():
                print(f"{value} : {key}")
        
        elif opcao == "sair":
            break

        else:
            print("OPÇÂO INVÁLIDA")

menu()

