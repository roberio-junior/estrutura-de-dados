def shell_sort(lista: list[int]) -> list[int]:
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            aux = lista[i]
            j = i
            while j >= gap and lista[j - gap] > aux:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = aux
        
        gap //= 2

    return lista

def encontrar_repetidos(lista: list[int]) -> list[int]:
    numeros_repetidos = []

    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1] and lista[i] not in numeros_repetidos:
            numeros_repetidos.append(lista[i])

    return numeros_repetidos

def contar_ocorrencias(valor: int, lista: list[int]) -> int:
    contador = 0

    for elemento in lista:
        if elemento == valor:
            contador += 1

    return contador

numeros = [3, 5, 2, 3, 8, 5, 1, 5]

lista_ordenada = shell_sort(numeros)
print("Lista ordenada:", lista_ordenada)

numeros_repetidos = encontrar_repetidos(lista_ordenada)

mensagens = []

for numero in numeros_repetidos:
    quantidade = contar_ocorrencias(numero, lista_ordenada)
    mensagens.append(f"{numero} aparece {quantidade}x")

saida = ", ".join(mensagens)

print("Duplicatas:", saida)
