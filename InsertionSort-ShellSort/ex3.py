import random
import math

def shell_sort(lista:list[int]) -> list[int]:
    n = len(lista)
    gap = math.ceil(n/2)
    while gap > 0:
        for i in range (gap, n):
            if lista[i] < lista[i-gap]:
                aux = lista[i]
                lista[i] = lista[i-gap]
                lista[i-gap] = aux
        gap -= 1
            
    return lista


def insertion(lista: list[int], indice: int,) -> list[int]:
    for i in range (indice, 0, - 1):
        if lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[int]) -> list[int]:
    for i in range (1, len(lista), 1):
        lista = insertion(lista, i)
            
    return lista



numeros = [random.randint(1, 10000) for _ in range(10000)]

shell_sort(numeros)
print(numeros)