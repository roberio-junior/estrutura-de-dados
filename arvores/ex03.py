from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)
# Função de percurso em pré-ordem
def pre_ordem(node):
    if node is None:
        return []
    
    # Visita o nó atual, depois a esquerda e depois a direita
    return [node.value] + pre_ordem(node.left) + pre_ordem(node.right)

preOrdem = pre_ordem(arvore)
print(preOrdem) 
