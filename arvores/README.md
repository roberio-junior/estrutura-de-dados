tree — árvore binária aleatória (sem ordem específica)

bst — árvore binária de busca (binary search tree), com ordenação

heap — heap (max ou min)

height — altura

is_perfect — define se o nó é completo ou não
 
is_max — define se cada nó é mairo do que os seu filhos

letters - define se a árvore vai ser composta por números


# PROPIEDADES
## root.height
Altura da árvore, ou seja, o maior nível de profundidade entre a raiz e as folhas.

## root.is_balanced
Se a árvore está balanceada (a diferença de altura entre subárvores esquerda e direita de qualquer nó é no máximo 1).

## root.is_bst
Se a árvore é uma árvore binária de busca (BST), ou seja, os valores seguem a regra BST para cada nó. 

## root.is_complete
Se a árvore é completa, significando que todos os níveis, exceto possivelmente o último, estão completamente preenchidos e as folhas do último nível estão o mais à esquerda possível. Aqui é True.

## root.is_max_heap
Se a árvore é um max heap (pai maior que os filhos).

## root.is_min_heap
Se a árvore é um min heap (pai menor que os filhos).

## root.is_perfect
Se a árvore é perfeita: todos os níveis estão completamente preenchidos e todas as folhas estão no mesmo nível. Aqui é False porque o último nível não está totalmente completo (a folha 3 está num nível mais alto? Na verdade, 3 está no nível 1 e é folha, enquanto 4 e 5 estão no nível 2, portanto não é perfeita).

## root.is_strict
Se a árvore é estrita (ou cheia): cada nó tem 0 ou 2 filhos (não tem nós com só um filho).

## root.leaf_count
Número de folhas (nós sem filhos).

## root.max_leaf_depth
Profundidade máxima das folhas.

## root.min_leaf_depth
Profundidade mínima das folhas. 

## root.max_node_value
Maior valor presente em algum nó. 

## root.min_node_value
Menor valor presente em algum nó.

## root.size
Número total de nós na árvore.

## root.properties
Retorna um dicionário com todas as propriedades da árvore, útil para pegar várias propriedades de uma vez.

## root.leaves
Lista dos nós folha

## root.levels
Lista dos nós por níveis

## inorder (em ordem)
Visita: esquerda → raiz → direita
Útil para: obter valores ordenados em árvores binárias de busca (BST)

# Percursos em profundidade (DFS):
## preorder (pré-ordem)
Visita: raiz → esquerda → direita
Útil para: copiar ou serializar árvores

## postorder (pós-ordem)
Visita: esquerda → direita → raiz
Útil para: deletar a árvore (ou liberar memória)

# Percurso em largura (BFS):
## levelorder (nível por nível)
Visita: nível por nível, da esquerda pra direita
Útil para: algoritmos de busca em largura, como calcular distância mínima