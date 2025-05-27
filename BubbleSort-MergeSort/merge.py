def merge_sort (lista: list[int]) -> list[int]:
    if len(lista) == 1:
        return lista
    metade  = len(lista) // 2
    return shell_sort(merge_sort(lista[:metade]) + merge_sort(lista[metade:]))

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

lista = [54,26,93,17,77,31,44,55,20]
print(merge_sort(lista))