# **BUBBLE SORT**

O **Bubble Sort** é um dos algoritmos de ordenação mais simples e intuitivos. Ele funciona comparando pares de elementos adjacentes e trocando-os de lugar se estiverem na ordem incorreta. Esse processo é repetido várias vezes até que a lista esteja completamente ordenada. O nome "bubble" (bolha) vem do comportamento dos maiores elementos, que "subem" gradualmente para o final da lista a cada iteração, como bolhas em um copo d’água.

## ⚙️ Funcionamento do Algoritmo

**Comparação e Troca:** A cada passagem pela lista, o algoritmo compara os elementos vizinhos e os troca se estiverem fora de ordem.
**Múltiplas Passagens:** O processo é repetido diversas vezes até que nenhuma troca seja mais necessária, o que significa que a lista está ordenada. A cada iteração completa, o maior elemento restante é colocado na sua posição final.

## Exemplo de código

```python
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

lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = bubble_sort(lista)
print(f"Lista ordenada: {lista_ordenada}")
```

---

# **MERGE SORT**

O **Merge Sort** é um algoritmo de ordenação eficiente e estável, baseado na técnica de **divisão e conquista**. Ele divide recursivamente a lista em sublistas menores até que cada sublista tenha apenas um elemento. Em seguida, essas sublistas são combinadas (ou "mescladas") de forma ordenada, até que toda a lista esteja organizada.

## ⚙️ Funcionamento do Algoritmo

**Divisão:** A lista é dividida ao meio recursivamente até que cada sublista tenha apenas um elemento.
**Conquista (Mesclagem):** As sublistas são então combinadas em ordem crescente, comparando os menores elementos de cada parte. Esse processo garante que a lista resultante também esteja ordenada.

## Exemplo de código

```python
def merge_sort (lista: list[int]) -> list[int]:
    if len(lista) == 1:
        return lista

    metade  = len(lista) // 2

    return shell_sort(merge_sort(lista[:metade]) + merge_sort(lista[metade:]))

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

lista = [54,26,93,17,77,31,44,55,20]
print("Lista ordenada:", merge_sort(lista))
```
