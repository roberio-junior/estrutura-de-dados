def verificar_palindromo():
    # recebe uma string
    entrada = input("Digite uma palavra: ")

    pilha = []

    # Empilha todos as letras
    for letra in entrada:
        pilha.append(letra)

    eh_palindromo = True

    # Compara a lista original com a versão invertida usando a pilha
    for letra in entrada:
        if letra != pilha.pop():  # desempilha o último e compara
            eh_palindromo = False
            break

    # Resultado
    if eh_palindromo:
        return print(True)
    else:
        return print(False)

# Executa a verificação
verificar_palindromo()
