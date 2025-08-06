from binarytree import bst, Node

def count_internal_nodes(node):
    if node is None:
        return 0
    # Se tem pelo menos um filho, é nó interno
    if node.left is not None or node.right is not None:
        return 1 + count_internal_nodes(node.left) + count_internal_nodes(node.right)
    else:
        # Nó folha, não conta
        return 0

# Criar uma BST aleatória com altura 4 (máximo 15 nós)
root = bst(height=4)

# Imprime a árvore
print(root)

# Contar nós internos
num_internos = count_internal_nodes(root)
print(f"Número de nós internos na BST: {num_internos}")
