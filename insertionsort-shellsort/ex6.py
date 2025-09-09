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

def mediana (lista: list[float]) -> list[float]:
    insertion_sort(lista)
    tamanho = len(lista)
    if tamanho % 2 == 1:
        return lista[tamanho // 2]
    else:
        mid = tamanho // 2
        return (lista[mid - 1] + lista[mid]) / 2
    return print(f" Notas ordenadas: {lista}\n", f"A média da turma é:{media:.2f}")

notas = [90.77, 88.52, 13.66, 33.4, 90.74]

print(mediana(notas))
 