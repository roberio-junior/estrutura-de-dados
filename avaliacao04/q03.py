from binarytree import bst

def total_de_nos(root):
    if root is None:
        return 0
    return 1 + total_de_nos(root.left) + total_de_nos(root.right)

def somar_nos(root):
    if root is None:
        return 0
    return root.value + somar_nos(root.left) + somar_nos(root.right)

def average_value(root):
    media = somar_nos(root)/total_de_nos(root)
    return media

# Criar uma BST aleatória com altura 4 (máximo 15 nós)
root = bst(height=2)

# Imprime a árvore
print(root)

# Contar nós internos
num_nos = total_de_nos(root)
soma = somar_nos(root)
media = average_value(root)
print(f"Número de nós internos na BST:{num_nos}")
print(f"Soma de todos os nós da BST: {soma}")
print(f"media dos nós: {media:.2f}")
