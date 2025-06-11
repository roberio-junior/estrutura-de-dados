import operator
# Dicionário que mapeia strings para operadores reais
operadores = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def pos_fixa(lista: list) -> float:
    pilha = []

    for i in range (len(lista)):
        if type(lista[i]) == int:
            pilha.append(lista[i])
            print(pilha)
        else:
            num1 = pilha.pop()
            num2 = pilha.pop()
            op = lista[i]
            print(f"{num2} {op} {num1}")
            resultado = operadores[op](num2, num1)
            pilha.append(resultado)

    return pilha[0]

lista = [5, 1, 2, '+', 4, '*', '+', 3, '-']

resultado = pos_fixa(lista)

print(f"Resultado da expressão pós-fixada {lista} é: {resultado}")