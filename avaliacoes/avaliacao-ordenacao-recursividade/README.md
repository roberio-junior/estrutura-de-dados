## Avaliação de Estrutura de Dados: Recursividade e Algoritmos de Ordenação

Professor: **Keylly Santos**

---

### Questão 1: Detectando Palíndromos com Ordenação
Duas palavras são palíndromos se podem ser lidas da mesma forma de trás para frente.  
Escreva uma função recursiva que verifique se uma palavra é palíndromo.  
Em seguida, organize uma lista de palavras, incluindo palíndromos e não-palíndromos, em ordem crescente (ordem alfabética) utilizando **insertion sort**.

**Entrada esperada:**

```python
["ana", "casa", "arara", "luz", "radar"]
```

**Saída esperada:**

```python
Lista ordenada: ["ana", "arara", "casa", "luz", "radar"]
Palíndromos identificados: ["ana", "arara", "radar"]
```

---

### Questão 2: Estatísticas com Recursividade
Implemente uma função recursiva para somar todos os elementos de um vetor de notas.  
Depois, ordene esse vetor com **insertion sort** e calcule a mediana.

**Entrada esperada:**

```python
[6.7, 8.5, 5.4, 9.0, 7.8]
```

**Saída esperada:**

```python
Soma total: X
Lista ordenada: [5.4, 6.7, 7.8, 8.5, 9.0]
Mediana: 7.8
```

---

### Questão 3: Vetor Ordenado? Use Recursão!
Você recebeu uma lista de números inteiros.  
Escreva uma função recursiva para verificar se a lista está ordenada em ordem crescente.  
Em seguida, ordene a lista usando **shell sort** caso não esteja ordenada.

**Entrada de exemplo:**

```python
[10, 15, 12, 20, 25]
```

**Saída esperada:**

```python
Está ordenado? False
Lista ordenada: [10, 12, 15, 20, 25]
```

---

### Questão 4: Verificação de Duplicatas e Ordenação
Implemente uma função (não recursiva) que conte quantas vezes um número aparece em uma lista.  
Depois, ordene a lista com **shell sort** e imprima os números que aparecem mais de uma vez.

**Entrada esperada:**

```python
[3, 5, 2, 3, 8, 5, 1, 5]
```

**Saída esperada:**

```python
Lista ordenada: [1, 2, 3, 3, 5, 5, 5, 8]
Duplicatas: 3 aparece 2x, 5 aparece 3x
```
