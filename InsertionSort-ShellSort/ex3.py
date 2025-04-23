import random

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

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2


numeros = [random.randint(1, 10000) for _ in range(10000)]

shellSort(numeros)
print(numeros)

numeros = [random.randint(1, 10000) for _ in range(10000)]

listaOrdenada = insertion_sort(numeros)
print(f"Lista ordenada: {listaOrdenada}")