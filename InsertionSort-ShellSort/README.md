# SHELL SORT
O **Shell sort**, também conhecido como “ordenação por incrementos diminutos”, é uma melhoria da ordenação por inserção. Ele funciona dividindo a lista original em várias sublistas, que são formadas a partir de elementos espaçados por um intervalo fixo, chamado de **gap** (ou incremento). Diferente da ordenação por inserção tradicional, que compara elementos adjacentes, o Shell sort compara elementos distantes entre si, o que acelera a movimentação de valores para posições mais próximas das corretas.

A chave do algoritmo está justamente na forma como esses **gaps** são escolhidos. Inicialmente, o **gap** é grande (por exemplo, **n/2**, onde **n** é o tamanho da lista) e vai sendo reduzido progressivamente (por exemplo, para **n/4**, **n/8**, até 1). Em cada etapa, os elementos separados pelo **gap** formam sublistas que são ordenadas usando o método de inserção. No final, quando o **gap** é 1, a lista já está quase ordenada, e a ordenação por inserção finaliza o processo com alta eficiência.

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

---

### 2. Ordenação de nomes com prioridade
Dada uma lista de tuplas (nome, idade) , ordene a lista pela idade (crescente). Em caso de idades iguais, preserve a ordem original dos nomes (estabilidade).

Dica: Use insertion sort, que é estável.

---

### 3. Análise de desempenho
Implemente uma função que compare o tempo de execução do insertion sort e do shell sort em uma lista de 10.000 números inteiros aleatórios. Qual é mais rápido?

---

### 4. Ordenando datas
Você recebeu uma lista de datas no formato DD/MM/AAAA . Ordene as datas em ordem crescente (mais antiga para mais recente) utilizando shell sort.

---

### 5. Detectando duplicatas
Ordene uma lista de números inteiros e retorne os elementos que aparecem mais de uma vez.

---

### 6. Mediana da turma
Implemente uma função que receba uma lista de notas, ordene com insertion sort, e retorne a mediana.

---

### 7. Ranking de vendas
Uma loja possui uma lista com (produto, unidades vendidas) . Ordene os produtos pelo número de unidades vendidas (ordem decrescente), usando shell sort.

---

### 8. Verificando anagramas
Duas palavras são anagramas se tiverem as mesmas letras em ordem diferente. Implemente uma função que, usando insertion sort, verifique se duas palavras são anagramas.

---

### 9. Organizando arquivos por tamanho
Dada uma lista com os tamanhos de arquivos (em MB), ordene-os do menor para o maior usando shell sort.

---

### 10. Estatísticas de uma pesquisa
Você recebeu as idades de 500 entrevistados. Ordene os dados e responda:
- Qual a menor idade?
- Qual a maior?
- Qual a idade mediana?

Use insertion sort para a ordenação.
