from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função recursiva para inserir um valor em uma árvore binária de busca (BST)
def insercao(root, value):
    # Caso a raiz esteja vazia, cria um novo nó com o valor e o retorna
    if root is None:
        return Node(value)
    
    # Se o valor for menor que o valor do nó atual, insere na subárvore esquerda
    if value < root.value:
        root.left = insercao(root.left, value)
    else:
        # Caso contrário, insere na subárvore direita
        root.right = insercao(root.right, value)
    
    # Retorna a raiz atualizada (necessária para manter os encadeamentos)
    return root

arvore = insercao(arvore, 5)
arvore = insercao(arvore, 2)
print(arvore)