from binarytree import bst, Node

def existe_caminho_com_soma(node, soma_alvo):
    if node is None:
        return False

    # Se é folha, verifica se o valor bate com o restante da soma
    if node.left is None and node.right is None:
        return node.value == soma_alvo

    # Subtrai o valor atual e verifica os caminhos à esquerda e à direita
    soma_restante = soma_alvo - node.value
    return (existe_caminho_com_soma(node.left, soma_restante) or
            existe_caminho_com_soma(node.right, soma_restante))

# Criar BST aleatória com altura 4
root = bst(height=4)

# Mostrar a árvore
print(root)

# Definir valor alvo (você pode mudar para testar)
alvo = 50

# Verificar se existe caminho com a soma igual ao alvo
exists = existe_caminho_com_soma(root, alvo)
print(f"Existe caminho com soma = {alvo}? {exists}")
