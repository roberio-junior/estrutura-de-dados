from binarytree import bst

def list_leaf_values(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.value]
    return list_leaf_values(root.left) + list_leaf_values(root.right)

# Criar BST aleatória com 10 nós
root = bst(height=4)

# Imprime a árvore
print(root)

# listar folhas
folhas = list_leaf_values(root)
print("Folhas na BST:", folhas)
