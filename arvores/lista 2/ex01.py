from binarytree import Node

def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    # Árvore vazia é BST
    if node is None:
        return True

    # Verifica se o valor do nó está dentro do intervalo permitido
    if not (min_val < node.value < max_val):
        return False

    # Recursivamente verifica subárvores esquerda e direita
    return (is_bst(node.left, min_val, node.value) and
            is_bst(node.right, node.value, max_val))


# Exemplo de uso:

# Criar uma árvore manualmente
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

print(is_bst(root))  # Deve imprimir True

# Alterar um nó para quebrar a regra
root.right.left = Node(8)
print(is_bst(root))  # Deve imprimir False pois 8 < 10, mas está à direita de 10
