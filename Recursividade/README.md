# **Recursividade**

Recursividade é uma técnica de definição ou construção de algoritmos onde uma função é definida em termos de si mesma. Ela resolve um problema ao dividi-lo em subproblemas de mesma natureza e complexidade reduzida.

## **Componentes de uma função recursiva**:

1. **Caso base**: É a condição de parada da função recursiva. Garante que a função não se chame indefinidamente.
2. **Chamada recursiva**: a função se chama com valores modificados até atingir o caso base.

## **Importância**

Recursão é usada para resolver problemas com estrutura naturalmente recursiva, como:

* Cálculo de [fatorial](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/fatorial.py)
* Sequência de [Fibonacci](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/fibonacci.py)
* Cálculo de [potência](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/potencia.py)

## **Desvantagens**

* Pode consumir muita memória de pilha.
* Em alguns casos, é menos eficiente que a versão iterativa.

## **Tipos de recursão**

* **Direta**: a função chama a si mesma diretamente
* **Indireta**: a função chama outra, que eventualmente chama a primeira

# Lista de Exercícios
## Parte 1 – Conceitos Básicos

### 1. Fatorial de um número
Implemente uma função recursiva que calcule o fatorial de um número inteiro positivo n.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex01.py)

---

### 2. Soma dos primeiros N números naturais
Crie uma função recursiva que receba um número n e retorne a soma de todos os números de 1 até n.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex02.py)

---
### 3. Fibonacci
Implemente uma função recursiva que retorne o n -ésimo termo da sequência de Fibonacci.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex03.py)

---
### 4. Potenciação
Implemente uma função recursiva que calcule a^b , onde a é a base e b o expoente.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex04.py)

---
## Parte 2 – Problemas Clássicos

### 5. Inverter uma string
Escreva uma função recursiva que inverta uma string.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex05.py)

---
### 6. Máximo divisor comum (MDC)
Crie uma função recursiva que calcule o MDC de dois números usando o algoritmo de Euclides.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex06.py)

---
### 7. Número de dígitos de um número
Escreva uma função recursiva que conte o número de dígitos de um número inteiro positivo.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex07.py)

---
### 8. Imprimir números decrescentes
Escreva uma função recursiva que imprima todos os números de n até 1.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex08.py)

---
## Parte 3 – Aplicações com vetores
### 9. Soma de elementos de um vetor
Escreva uma função recursiva que some todos os elementos de um vetor de inteiros.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex09.py)

---
### 10. Verificar se uma palavra é palíndromo
Implemente uma função recursiva que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente).

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex10.py)

---
### 11. Imprimir elementos de um vetor ao contrário
Crie uma função recursiva que imprima os elementos de um vetor de trás para frente.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex11.py)

---

### 12. Exercício com lógica de ordenação
Verifique se um vetor está ordenado implementando uma função recursiva que verifique se um vetor de inteiros está ordenado em ordem crescente.
> Exemplo: [1, 2, 3, 4, 5] → True ; [1, 3, 2, 4] → False .

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/Recursividade/ex12.py)
