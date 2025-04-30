def insertion(lista: list[tuple], indice: int,) -> list[tuple]:
    for i in range (indice, 0, - 1):
        if lista[i][1] < lista[i-1][1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[tuple]) -> list[tuple]:
    for i in range (1, len(lista), 1):
        insertion(lista, i)
            
    return lista
 
pessoas = [("Robério", 21), ("joão", 30), ("Júlia", 25), ("Pedro", 28)]
print(f"Lista desordenada: {pessoas}")

listaOrdenada = insertion_sort(pessoas)
print(f"Lista ordenada: {listaOrdenada}")
