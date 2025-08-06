from binarytree import bst, Node

arvore = bst(height=4)
print(arvore)

# Função de percurso em pós-ordem (post-order)
def post_order(node):
    if node is None:
        return []
    
    # Esquerda -> Direita -> Raiz
    return post_order(node.left) + post_order(node.right) + [node.value]

postOder = post_order(arvore)
print(postOder)
