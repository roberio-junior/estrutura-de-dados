# Função que combina os conceitos de Merge Sort e Shell Sort
def merge_sort (lista: list[int]) -> list[int]:
    # Se a lista tiver apenas um elemento, ela já está ordenada
    if len(lista) == 1:
        return lista
    # Divide a lista ao meio
    metade  = len(lista) // 2
    # Aplica merge_sort recursivamente nas duas metades
    # Junta as duas metades ordenadas e ordena o resultado com shell_sort
    return shell_sort(merge_sort(lista[:metade]) + merge_sort(lista[metade:]))

# Função de ordenação Shell Sort
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

# Lista de exemplo
lista = [54,26,93,17,77,31,44,55,20]

# Imprime a lista original ordenada utilizando a função merge_sort
print("Lista ordenada:", merge_sort(lista))