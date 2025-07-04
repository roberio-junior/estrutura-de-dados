def verificar_palindromo():
    # Lê a sequência como uma string e separa os números em uma lista
    entrada = input("Digite os números separados por espaço: ")
    numeros = entrada.split()

    pilha = []

    # Empilha todos os números
    for num in numeros:
        pilha.append(num)

    eh_palindromo = True

    # Compara a lista original com a versão invertida usando a pilha
    for num in numeros:
        if num != pilha.pop():  # desempilha o último e compara
            eh_palindromo = False
            break

    # Resultado
    if eh_palindromo:
        print("A sequência é um palíndromo.")
    else:
        print("A sequência não é um palíndromo.")


# Executa a verificação
verificar_palindromo()
