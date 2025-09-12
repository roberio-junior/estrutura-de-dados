## 1. Pilhas (Stacks)

### 🔹 Conceito

Uma **pilha** é uma estrutura de dados do tipo **LIFO** (*Last In, First Out*), ou seja:
➡️ o último elemento que entra é o primeiro a sair.

É como uma pilha de pratos: você só consegue pegar o prato que está no topo.

### 🔹 Operações principais

* **push** → adiciona um elemento no topo da pilha.
* **pop** → remove o elemento do topo da pilha.
* **peek/top** → consulta o elemento do topo sem removê-lo.
* **isEmpty** → verifica se a pilha está vazia.

### 🔹 Exemplo visual

```
Topo -> [5]
        [3]
        [1] <- Base
```

* `push(7)` → empilha o 7 no topo.
* `pop()` → retira o 5 (o último que entrou).
* 
### 🔹 Operações principais

* **push** → adiciona um elemento no topo da pilha.
* **pop** → remove o elemento do topo da pilha.
* **peek/top** → consulta o elemento do topo sem removê-lo.
* **isEmpty** → verifica se a pilha está vazia.

---

## 2. Filas (Queues)

### 🔹 Conceito

Uma **fila** é uma estrutura de dados do tipo **FIFO** (*First In, First Out*), ou seja:
➡️ o primeiro elemento que entra é o primeiro a sair.

É como uma fila de banco ou supermercado: quem chega primeiro é atendido primeiro.

### 🔹 Operações principais

* **enqueue** → adiciona um elemento no fim da fila.
* **dequeue** → remove o elemento do início da fila.
* **peek/front** → consulta o elemento da frente sem removê-lo.
* **isEmpty** → verifica se a fila está vazia.

### 🔹 Exemplo visual

```
Frente -> [1] [3] [5] <- Traseira
```

* `enqueue(7)` → entra na traseira, fica: `[1] [3] [5] [7]`.
* `dequeue()` → remove o 1 (o primeiro que entrou).

---

## 📘 Lista de Exercícios Práticos – Implementação com Pilhas e Filas

## Parte 1: Pilhas

### 1. 📌 Cálculo de Expressão Pós-fixa

Implemente um algoritmo que leia uma expressão matemática em notação pós-fixa (ex: `"5 1 2 + 4 * + 3 -"`) e calcule seu resultado utilizando uma pilha.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex01.py)

### 2. 📌 Simulador de Navegador com Botões Voltar e Avançar

Crie um programa que simule o funcionamento do botão “voltar” e “avançar” em um navegador, usando duas pilhas para gerenciar o histórico de páginas visitadas.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex02.py)

### 3. 📌 Verificação de Expressão Balanceada

Desenvolva uma função que, utilizando uma pilha, verifique se uma expressão com parênteses, colchetes e chaves está corretamente balanceada.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex03.py)

### 4. 📌 Inversão de String com Pilha

Escreva um algoritmo que receba uma string e use uma pilha para inverter seus caracteres.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex04.py)

### 5. 📌 Simulação de Recursão para Cálculo de Fatorial

Elabore um programa que simule a execução de chamadas recursivas para o cálculo do fatorial de um número utilizando pilha, sem utilizar recursão nativa.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex05.py)

### 6. 📌 Editor de Texto com Desfazer Ações

Crie um programa que simule um editor de texto com a funcionalidade de desfazer ações. Cada ação (como escrever ou apagar) deve ser registrada em uma pilha e desfeita em ordem inversa à execução.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex06.py)

### 7. 📌 Conversão de Expressão Infixa para Pós-fixa

Desenvolva um algoritmo que converta uma expressão matemática da forma infixa (com operadores entre operandos) para a forma pós-fixa, utilizando uma pilha para controlar operadores e parênteses.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex07.py)

### 8. 📌 Pilha com Capacidade Limitada

Implemente uma estrutura de pilha com capacidade limitada. O programa deve informar quando a pilha estiver cheia ou vazia ao tentar inserir ou remover elementos.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex08.py)

### 9. 📌 Controle de Estados em Jogos

Faça um programa que armazene os estados de um jogo em uma pilha para permitir que o jogador "volte no tempo" para um estado anterior. Simule uma sequência de inserções e remoções.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex09.py)

### 10. 📌 Verificação de Palíndromo com Pilha

Elabore um algoritmo que leia uma sequência de números e use uma pilha para identificar se ela forma um palíndromo (ex: 1, 2, 3, 2, 1).

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex010.py)

---

## Parte 2: Filas

### 11. 📌 Fila de Atendimento em Supermercado

Implemente um algoritmo que simule a fila de atendimento de um caixa de supermercado, com operações de chegada de clientes, atendimento e exibição do estado atual da fila.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex11.py)

### 12. 📌 Fila de Impressão de Arquivos

Crie um programa que simule o envio de arquivos para impressão em uma fila. Cada arquivo tem um nome e uma quantidade de páginas. A fila deve processar os arquivos por ordem de chegada.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex12.py)

### 13. 📌 Fila Circular com Tamanho Fixo

Desenvolva um programa que utilize uma fila circular com tamanho fixo. Implemente as operações de inserção e remoção, e mostre o comportamento da fila quando ela estiver cheia ou vazia.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex13.py)

### 14. 📌 Embarque e Desembarque de Passageiros

Faça um algoritmo que simule o embarque e desembarque de passageiros em um ônibus, respeitando a ordem de chegada para embarque.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex14.py)

### 15. 📌 Fila de Requisições ao Servidor

Implemente um sistema de controle de requisições a um servidor, onde cada requisição entra em uma fila e é processada na ordem de chegada.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex15.py)

### 16. 📌 Sistema de Senhas de Banco

Elabore um programa que simule a retirada e o atendimento de senhas em um banco. Cada senha deve ser chamada por ordem de chegada, com exibição da fila a cada atendimento.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex16.py)

### 17. 📌 Busca em Largura (BFS) em Labirinto

Escreva um algoritmo que simule a busca em largura (BFS) em uma matriz representando um labirinto, utilizando fila para armazenar as posições a serem exploradas.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex17.py)

### 18. 📌 Fila de Exibição de Mensagens em Chat

Desenvolva um programa para gerenciar a exibição de mensagens em um chat. Mensagens devem ser exibidas na ordem em que foram recebidas.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex18.py)

### 19. 📌 Agendamento de Tarefas com Fila

Crie um sistema de agendamento de tarefas usando uma fila. Cada tarefa tem um nome e um tempo estimado. As tarefas devem ser executadas por ordem de chegada.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex19.py)

### 20. 📌 Comparação entre Fila e Pilha no Atendimento

Implemente um algoritmo que compare o comportamento de uma fila com o de uma pilha em situações de atendimento ao público. Mostre os diferentes resultados usando os mesmos dados de entrada.

👉 [Clique aqui para ver a resolução completa](https://github.com/roberio-junior/estrutura-de-dados/blob/main/pilha-fila/ex20.py)
