from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função de percurso em ordem (in-order)
def in_order(node):
    if node is None:
        return []
    
    # Esquerda -> Raiz -> Direita
    return in_order(node.left) + [node.value] + in_order(node.right)

inOrder = in_order(arvore)
print(inOrder)
