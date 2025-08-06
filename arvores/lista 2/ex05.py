from binarytree import bst, Node
from collections import deque  # Fila eficiente

def percurso_em_nivel(root):
    if root is None:
        return []

    fila = deque()
    visitados = []

    fila.append(root)

    while fila:
        no_atual = fila.popleft()  # Remove o primeiro da fila
        visitados.append(no_atual.value)

        # Adiciona os filhos à fila, se existirem
        if no_atual.left:
            fila.append(no_atual.left)
        if no_atual.right:
            fila.append(no_atual.right)

    return visitados

# Criar BST aleatória com altura 4
root = bst(height=4)

# Mostrar a árvore
print(root)

# Executar percurso em nível
sequencia = percurso_em_nivel(root)
print("Sequência de nós visitados em nível:", sequencia)
