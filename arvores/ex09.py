from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função para encontrar o valor máximo
def encontrar_maximo(arvore):
    if arvore is None:
        return None
    atual = arvore
    while atual.right:
        atual = atual.right
    return atual.value

# Mostrar o valor máximo
maximo = encontrar_maximo(arvore)
print(f"Valor máximo na BST: {maximo}")