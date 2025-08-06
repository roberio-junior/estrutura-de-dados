from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função para buscar um valor em uma BST
def busca(node, value):
    if node is None:
        return False  # Valor não encontrado
    
    if node.value == value:
        return True  # Valor encontrado
    
    if value < node.value:
        return busca(node.left, value)
    else:
        return busca(node.right, value)

found = busca(arvore, 6)

# Exibe o resultado da busca
if found:
    print(f"Valor {"6"} encontrado na árvore.")
else:
    print(f"Valor {"6"} **não** encontrado na árvore.")