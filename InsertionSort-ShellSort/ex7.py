def shell_sort(lista: list[tuple]) -> list[tuple]:
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            aux = lista[i]
            j = i
            while j >= gap and lista[j - gap][1] < aux[1]:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = aux

        gap //= 2

    return lista

produtos = [("Camisas", 21), ("Calças", 25), ("Tênis", 28), ("Cintos", 30)]
print(f"Lista desordenada: {produtos}")

listaOrdenada = shell_sort(produtos)
print(f"Lista ordenada: {listaOrdenada}")
