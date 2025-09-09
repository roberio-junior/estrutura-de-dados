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
shell_sort(lista)
print(lista)

tamanhos = [500, 150, 250, 30, 1000, 750, 200, 400]
tamanhos_ordenados = shell_sort(tamanhos)
print(f"Tamanhos dos arquivos ordenados: {tamanhos_ordenados}")
