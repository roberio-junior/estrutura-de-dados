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
    repetidos = []
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1] and lista[i] not in repetidos:
            repetidos.append(lista[i])
    return print(f"Elementos que aparecem mais de uma vez: {repetidos}")

vetor = [3, 5, 2, 3, 8, 5, 1, 5]

listaOrdenada = shell_sort(vetor)
print(listaOrdenada)
repetidos = encontrar_repetidos(vetor)

