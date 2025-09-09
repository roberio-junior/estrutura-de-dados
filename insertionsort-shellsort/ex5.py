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

    return print(f"lista ordenada: {lista}")


def encontrar_repetidos(lista: list[int]) -> list[int]:
    repetidos = []
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1] and lista[i] not in repetidos:
            repetidos.append(lista[i])
    return print(f"Elementos que aparecem mais de uma vez: {repetidos}")

lista = [54,26,93,44,93,17,77,31,44,31,55,20,54,93]
shell_sort(lista)
encontrar_repetidos(lista)
