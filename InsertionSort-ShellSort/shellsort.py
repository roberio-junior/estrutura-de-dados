def shell_sort(lista:list[int]) -> list[int]:
    n = len(lista)
    gap = n//2
    while gap > 0:
        for i in range (gap, n):
            if lista[i] < lista[i-gap]:
                aux = lista[i]
                lista[i] = lista[i-gap]
                lista[i-gap] = aux
            print(lista, gap)
        gap -= 1
            
    return lista

listaDesordenada = [8, 4, 1, 7, 2, 6, 3, 5,0]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = shell_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")



# correta
def shell_sort(lista: list[int]) -> list[int]:
    n = len(lista)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            aux = lista[i]
            print("aux = lista[i]")
            print(f"aux = {lista[i]}\n")

            j = i
            print("j = i")
            print(f"j = {i}\n")

            while j >= gap and lista[j - gap] > aux:
                print("while j >= gap and lista[j - gap] > aux:")
                print(f"while {j} >= {gap} and {lista[j - gap]} > {aux}:\n")

                print("lista[j] = lista[j - gap]")
                print(f"{lista[j]} = {lista[j - gap]}\n")
                lista[j] = lista[j - gap]

                print("j -= gap")
                print(f"{j} -= {gap}\n")
                j -= gap

            print("lista[j] = aux")
            print(f"{lista[j]} = {aux}\n")
            lista[j] = aux

            print(lista, f"gap: {gap}")

        print("gap //= 2")
        print(f"\n")
        gap //= 2

    return lista

listaDesordenada = [8, 4, 1, 7, 2, 6, 3, 5]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = shell_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")