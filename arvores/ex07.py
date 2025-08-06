from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

def remover(arvore, valor):
    if arvore is None:
        return None

    if valor < arvore.value:
        arvore.left = remover(arvore.left, valor)
    elif valor > arvore.value:
        arvore.right = remover(arvore.right, valor)
    else:
        # Caso 1: Nó sem filhos
        if arvore.left is None and arvore.right is None:
            return None
        # Caso 2: Um filho
        elif arvore.left is None:
            return arvore.right
        elif arvore.right is None:
            return arvore.left
        # Caso 3: Dois filhos
        else:
            # Encontra o menor valor da subárvore direita (sucessor)
            sucessor = arvore.right
            while sucessor.left:
                sucessor = sucessor.left
            arvore.value = sucessor.value
            arvore.right = remover(arvore.right, sucessor.value)
    
    return arvore

arvore = remover(arvore, 5)
print(arvore)

