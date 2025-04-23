def insertion(lista: list[float], indice: int,) -> list[int]:
    for i in range (indice, 0, - 1):
        if lista[i] > lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[int]) -> list[int]:
    for i in range (1, len(lista), 1):
        insertion(lista, i)
            
    return lista

listaDesordenada = [6.7, 8.5, 5.4, 9.0, 7.8]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = insertion_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")