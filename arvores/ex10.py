from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função para calcular altura
def altura(arvore):
    if arvore is None:
        return -1
    else:
        altura_esquerda = altura(arvore.left)
        altura_direita = altura(arvore.right)
        return 1 + max(altura_esquerda, altura_direita)

# Calculando a altura da árvore
h = altura(arvore)
print(f"Altura da BST: {h}")