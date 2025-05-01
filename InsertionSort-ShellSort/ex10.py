import random

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

def mediana (lista: list[int]):
    tamanho = len(lista)
    if tamanho % 2 == 1:
        return lista[tamanho // 2]
    else:
        mid = tamanho // 2
        return (lista[mid - 1] + lista[mid]) // 2

idades = [random.randint(5, 111) for _ in range(500)]

idadesOrdenadas = shell_sort(idades)
idadeMediana = mediana(idadesOrdenadas)

print(f"Menor idade: {idadesOrdenadas[0]}\nMaior idade: {idadesOrdenadas[len(idadesOrdenadas)-1]}\nIdade média: {idadeMediana}")
