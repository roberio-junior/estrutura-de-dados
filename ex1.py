def insertion(lista: list[int], indice: int,) -> list[int]:
    for i in range (indice, 1, - 1): # troca o 1 por 0
        if lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[int]) -> list[int]:
    for i in range (1, len(lista) -1, 1): # tira o "-1"
        lista = insertion(lista, i)
            
    return lista

# EXEMPLO 1:
lil = [1,5,6,4]
print(f"Antes: {lil}")

#insere o item da posição 3 de forma ordenada
li2 = insertion(lil, 3)
print(f"Depois: {li2}\n")

# EXEMPLO 2:
listaDesordenada = [20, 9, 13, 16, 21, 32, 12]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = insertion_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")