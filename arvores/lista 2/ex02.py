from binarytree import bst, build, Node

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# Criar BST aleatória com 10 nós
root = bst(height=4)

# Imprime a árvore (Node tem __str__ que mostra a estrutura)
print(root)

# Contar o número de folhas
num_folhas = count_leaves(root)
print(f"Número de folhas na BST: {num_folhas}")
