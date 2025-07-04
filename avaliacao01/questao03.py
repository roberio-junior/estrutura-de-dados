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


def verificar_vetor_ordenado(vetor: list, tamanho: int) -> str:
  if tamanho <= 1:
    return True
  
  if vetor[tamanho] < vetor[tamanho - 1]:
    return False
  
  return verificar_vetor_ordenado(vetor, tamanho - 1)


vetor = [10, 15, 12, 20, 25]

verificacao = verificar_vetor_ordenado(vetor, len(vetor)-1)
if verificacao == False:
  listaOrdenada = shell_sort(vetor)
else: 
   listaOrdenada = vetor

print(f"Está ordenado? {verificacao}")
print(f"Lista ordenada: {listaOrdenada}")
