def fatorial_com_pilha(n):
    pilha = []

    # Empilha os valores de n até 1 (caso base)
    while n > 1:
        pilha.append(n)
        n -= 1

    # Caso base: fatorial de 1 é 1
    fatorial = 1

    # Desempilha e calcula o produto
    while pilha:
        valor = pilha.pop()
        fatorial *= valor

    # Retorna o fatorial
    return fatorial


# Teste
num = 5
print(f"Fatorial de {num} é: {fatorial_com_pilha(num)}")
