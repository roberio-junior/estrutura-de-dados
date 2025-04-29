# import math

# def shell_sort(lista:list[int]) -> list[int]:
#     n = len(lista)
#     gap = math.ceil(n/2)
#     while gap > 0:
#         for i in range (gap, n):
#             if lista[i] < lista[i-gap]:
#                 aux = lista[i]
#                 lista[i] = lista[i-gap]
#                 lista[i-gap] = aux
#         gap //= 2
            
#     return lista

# listaDesordenada = [5, 4, 3, 2, 1]
# print(f"Lista desordenada: {listaDesordenada}")

# listaOrdenada = shell_sort(listaDesordenada)
# print(f"Lista ordenada: {listaOrdenada}")


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

        
        print("Após incrementos de tamanho",gap," a lista é:",lista)
        gap //= 2

    return lista

listaDesordenada = [8, 4, 1, 7, 2, 6, 3, 5]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = shell_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")