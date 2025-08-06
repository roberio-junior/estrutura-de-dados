from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função para encontrar o valor mínimo
def encontrar_minimo(arvore):
    if arvore is None:
        return None
    atual = arvore
    while atual.left:
        atual = atual.left
    return atual.value

# Exibindo o valor mínimo
minimo = encontrar_minimo(arvore)
print(f"Valor mínimo na BST: {minimo}")