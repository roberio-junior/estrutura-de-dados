def insertion(lista: list[float], indice: int,) -> list[float]:
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


def soma_vetores(lista: list ) -> float:
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_vetores(lista[1:])


def mediana (lista: list[float]) -> list[float]:
    insertion_sort(lista)
    tamanho = len(lista)
    if tamanho % 2 == 1:
        return lista[tamanho // 2]
    else:
        mid = tamanho // 2
        return (lista[mid - 1] + lista[mid]) / 2


vetor = [6.7, 8.5, 5.4, 9.0, 7.8]

resultado = soma_vetores(vetor)
listaOrdenada = insertion_sort(vetor)
mediana = mediana(vetor)

print(f"Soma total: {resultado}.")
print(f"Lista ordenada: {listaOrdenada}")
print(f"Mediana: {mediana}")