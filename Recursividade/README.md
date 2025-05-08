# **Recursividade**

Recursividade é uma técnica de definição ou construção de algoritmos onde uma função é definida em termos de si mesma. Ela resolve um problema ao dividi-lo em subproblemas de mesma natureza e complexidade reduzida.

---

## **Componentes de uma função recursiva**:

1. **Caso base**: É a condição de parada da função recursiva. Garante que a função não se chame indefinidamente.
2. **Chamada recursiva**: a função se chama com valores modificados até atingir o caso base.

---

## **Importância**

Recursão é usada para resolver problemas com estrutura naturalmente recursiva, como:

* Cálculo de [fatorial](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/fatorial.py])
* Sequência de [Fibonacci](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/fibonacci.py)
* Cálculo de [potência](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/potencia.py)

---

## **Desvantagens**

* Pode consumir muita memória de pilha.
* Em alguns casos, é menos eficiente que a versão iterativa.

---

## **Tipos de recursão**

* **Direta**: a função chama a si mesma diretamente
* **Indireta**: a função chama outra, que eventualmente chama a primeira

---
