# Insertion Sort
O **Insertion Sort** é baseado na ideia de inserir elementos em uma sequência já ordenada. A cada iteração, um novo elemento é comparado com os anteriores e inserido na posição correta, mantendo a ordem crescente. Essa abordagem é semelhante à forma como organizamos cartas na mão: pegamos uma carta e a colocamos no lugar apropriado entre as que já estão ordenadas.
## ⚙️ Funcionamento do Algoritmo
1. Inserção Ordenada: Considere um array onde os primeiros N - 1 elementos estão ordenados, e o último precisa ser inserido na posição correta. O algoritmo compara esse último elemento com os anteriores e realiza trocas até que ele esteja na posição adequada.​
2. Aplicação Repetitiva: O Insertion Sort aplica essa inserção ordenada repetidamente, começando do segundo elemento até o final do array. A cada passo, ele garante que a sublista até o índice atual esteja ordenada.
## Exemplo de código
```python
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

listaDesordenada = [20, 9, 13, 16, 21, 32, 12]
listaOrdenada = insertion_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")
```
# SHELL SORT
O **Shell sort**, também conhecido como “ordenação por incrementos diminutos”, é uma melhoria da ordenação por inserção. Ele funciona dividindo a lista original em várias sublistas, que são formadas a partir de elementos espaçados por um intervalo fixo, chamado de **gap** (ou incremento). Diferente da ordenação por inserção tradicional, que compara elementos adjacentes, o Shell sort compara elementos distantes entre si, o que acelera a movimentação de valores para posições mais próximas das corretas.
## ⚙️ Funcionamento do Algoritmo
A chave do algoritmo está justamente na forma como esses **gaps** são escolhidos. Inicialmente, o **gap** é grande (por exemplo, **n/2**, onde **n** é o tamanho da lista) e vai sendo reduzido progressivamente (por exemplo, para **n/4**, **n/8**, até 1). Em cada etapa, os elementos separados pelo **gap** formam sublistas que são ordenadas usando o método de inserção. No final, quando o **gap** é 1, a lista já está quase ordenada, e a ordenação por inserção finaliza o processo com alta eficiência.

## Exemplo de código
A seguinte chamada da função `shellSort` mostra as listas parcialmente ordenadas depois de cada incremento, com a ordenação final sendo uma ordenação por inserção com incremento de um.

```python
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

        
        print("Após incrementos de tamanho",gap," a lista é:",lista)
        gap //= 2

    return lista

lista = [54,26,93,17,77,31,44,55,20]
shell_sort(lista)
print(lista)
```

# 📋 Lista de Exercícios – Algoritmos de Ordenação (Insertion Sort e Shell Sort)

### 1. Ordenando notas
Dada uma lista com as notas finais dos alunos de uma turma, ordene-as em ordem decrescente utilizando insertion sort.

Exemplo de entrada: [6.7, 8.5, 5.4, 9.0, 7.8]

Saída esperada: [9.0, 8.5, 7.8, 6.7, 5.4]

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex1.py)

---

### 2. Ordenação de nomes com prioridade
Dada uma lista de tuplas (nome, idade) , ordene a lista pela idade (crescente). Em caso de idades iguais, preserve a ordem original dos nomes (estabilidade).

Dica: Use insertion sort, que é estável.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex2.py)

---

### 3. Análise de desempenho
Implemente uma função que compare o tempo de execução do insertion sort e do shell sort em uma lista de 10.000 números inteiros aleatórios. Qual é mais rápido?

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex3.py)

---

### 4. Ordenando datas
Você recebeu uma lista de datas no formato DD/MM/AAAA . Ordene as datas em ordem crescente (mais antiga para mais recente) utilizando shell sort.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex4.py)

---

### 5. Detectando duplicatas
Ordene uma lista de números inteiros e retorne os elementos que aparecem mais de uma vez.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex5.py)

---

### 6. Mediana da turma
Implemente uma função que receba uma lista de notas, ordene com insertion sort, e retorne a mediana.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex6.py)

---

### 7. Ranking de vendas
Uma loja possui uma lista com (produto, unidades vendidas) . Ordene os produtos pelo número de unidades vendidas (ordem decrescente), usando shell sort.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex7.py)

---

### 8. Verificando anagramas
Duas palavras são anagramas se tiverem as mesmas letras em ordem diferente. Implemente uma função que, usando insertion sort, verifique se duas palavras são anagramas.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex8.py)

---

### 9. Organizando arquivos por tamanho
Dada uma lista com os tamanhos de arquivos (em MB), ordene-os do menor para o maior usando shell sort.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex9.py)

---

### 10. Estatísticas de uma pesquisa
Você recebeu as idades de 500 entrevistados. Ordene os dados e responda:
- Qual a menor idade?
- Qual a maior?
- Qual a idade mediana?

Use insertion sort para a ordenação.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/InsertionSort-ShellSort/ex10.py)
