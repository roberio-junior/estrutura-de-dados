from binarytree import bst, Node

# Função auxiliar para calcular altura de um nó
def calcular_altura(node):
    if node is None:
        return -1  # altura de árvore vazia é -1 (convenção comum)
    return 1 + max(calcular_altura(node.left), calcular_altura(node.right))

# Função principal para verificar se a árvore é balanceada
def esta_balanceada(node):
    if node is None:
        return True  # árvore vazia é balanceada

    # Calcula a altura das subárvores esquerda e direita
    left_height = calcular_altura(node.left)
    right_height = calcular_altura(node.right)

    # Verifica se a diferença de altura é maior que 1
    if abs(left_height - right_height) > 1:
        return False

    # Verifica se as subárvores também são balanceadas
    return esta_balanceada(node.left) and esta_balanceada(node.right)

# Criar uma BST aleatória com altura 4
root = bst(height=4)

# Mostrar a árvore
print(root)

# Verificar se está balanceada
print("Árvore está balanceada?", esta_balanceada(root))
