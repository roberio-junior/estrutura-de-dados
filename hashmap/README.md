## Principais conceitos

1. **Hash / hashing**

   * Hashing é transformar uma chave (por exemplo, string, número, ou outro) em um valor geralmente de tamanho fixo, para facilitar o armazenamento e recuperação. ([DataCamp][1])
   * A função hash deve devolver sempre o *mesmo* hash para a mesma entrada. ([DataCamp][1])

2. **Hashmap / hashtable**

   * Estrutura de dados que guarda pares *chave → valor* e permite operações rápidas (inserção, busca, remoção). ([DataCamp][1])
   * Usa-se uma tabela (“array de buckets”) onde cada chave, através de uma função hash, é mapeada para um índice. ([DataCamp][1])

3. **Funções hash comuns**
   Vários métodos para gerar hashes, com vantagens e desvantagens:

   | Método                     | Descrição básica                                                                                   |
   | -------------------------- | -------------------------------------------------------------------------------------------------- |
   | Divisão                    | Usa o resto da divisão da chave pelo tamanho da tabela como hash. ([DataCamp][1])                  |
   | Quadrado meio (mid-square) | Elevar ao quadrado a chave e pegar os dígitos do meio como hash. ([DataCamp][1])                   |
   | Multiplicação              | Multiplicar a chave por um número real grande, usar a parte fracionária. ([DataCamp][1])           |
   | Dobragem (folding)         | Dividir a chave em partes, somá-las, depois modularizar (resto) para obter índice. ([DataCamp][1]) |

---

## Hashmaps em Python: dicionários

* O tipo nativo `dict` do Python é uma implementação de hashmap. ([DataCamp][1])
* Características importantes:

  1. **Mutabilidade**: podemos adicionar, remover ou alterar pares (chave-valor) após a criação. ([DataCamp][1])
  2. **Ordem**: nas versões antigas (< 3.6) não se garantia ordem; desde o **Python 3.7**, os dicionários preservam a ordem de inserção das chaves. ([DataCamp][1])
  3. **Chaves imutáveis**: tipos mutáveis (listas, por exemplo) não podem ser usados como chaves, pois o hash poderia mudar. ([DataCamp][1])
  4. **Chaves únicas**: se uma chave for repetida no momento da criação, a última ocorrência sobrescreve as anteriores. ([DataCamp][1])

---

## Operações comuns com dicionários

* **Criar dicionário** (`{chave: valor, ...}` ou `dict()`) ([DataCamp][1])
* **Buscar por chave**: `dict[chave]`, ou `dict.get(chave)` (o `.get()` não lança erro caso a chave não exista, retornando `None` ou valor default) ([DataCamp][1])
* **Adicionar / atualizar**: usando a sintaxe `dict[chave] = valor` ([DataCamp][1])
* **Remover**: com `del dict[chave]` ou `.clear()` para limpar todos os itens ([DataCamp][1])
* **Iterar**:

  * `.items()` retorna pares `(chave, valor)` iteráveis.
  * `.keys()` e `.values()` para chaves e valores separadamente. ([DataCamp][1])

---
