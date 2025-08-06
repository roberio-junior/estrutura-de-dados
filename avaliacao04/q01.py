from binarytree import bst

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

# Função auxiliar para calcular altura de um nó
def calcular_altura(root):
    if root is None:
        return -1  # altura de árvore vazia é -1 (convenção comum)
    return 1 + max(calcular_altura(root.left), calcular_altura(root.right))

# Função principal para verificar se a árvore é balanceada
def is_height_balanced(root):
    if root is None:
        return True  # árvore vazia é balanceada

    # Calcula a altura das subárvores esquerda e direita
    left_height = calcular_altura(root.left)
    right_height = calcular_altura(root.right)

    # Verifica se a diferença de altura é maior que 1
    if abs(left_height - right_height) > 1:
        return False

    # Verifica se as subárvores também são balanceadas
    return is_height_balanced(root.left) and is_height_balanced(root.right)

arvore = bst(height=4, is_perfect=True)
print(arvore)

# Verificar se está balanceada
print("Árvore está balanceada?", is_height_balanced(arvore))

arvore = remover(arvore, 5)
print(arvore)
print("Árvore está balanceada?", is_height_balanced(arvore))
