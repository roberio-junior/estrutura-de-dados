import random
import time

def bubble_sort (lista: list[int]) -> list[int]:
    n = len(lista)

    while n > 0:
        for i in range (0, n- 1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
        n-=1
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

def tempo():
    numeros =list(range(1000000, 1, -1))

    listaShell = list(numeros)
    listaInsertion = list(numeros)

    start_time = time.time()
    shell_sort(listaShell)
    shell_duration = time.time() - start_time
    print(f"Shell Sort levou {shell_duration:.5f} segundos.")

    start_time = time.time()
    insertion_sort(listaInsertion)
    insertion_duration = time.time() - start_time
    print(f"Insertion Sort levou {insertion_duration:.5f} segundos.")

tempo()

