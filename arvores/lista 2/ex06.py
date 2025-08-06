from binarytree import bst, Node

def somar_nos(node):
    if node is None:
        return 0
    return node.value + somar_nos(node.left) + somar_nos(node.right)

# Criar uma BST aleatória com altura 4
root = bst(height=4)

# Mostrar a árvore
print(root)

# Calcular a soma de todos os nós
total = somar_nos(root)
print("Soma de todos os nós da BST:", total)
