from binarytree import Node

def construir_bst_preordem(preorder):
    # Função auxiliar com limites para o valor do nó (min_val, max_val)
    def construir_util(indice, min_val, max_val):
        # Se ultrapassar a lista, retorna None e índice atual
        if indice[0] == len(preorder):
            return None

        val = preorder[indice[0]]

        # Se o valor está fora do intervalo permitido, não pode estar aqui
        if val < min_val or val > max_val:
            return None

        # Cria o nó atual e avança o índice
        no = Node(val)
        indice[0] += 1

        # Constroi subárvore esquerda com valores menores que val
        no.left = construir_util(indice, min_val, val - 1)

        # Constroi subárvore direita com valores maiores que val
        no.right = construir_util(indice, val + 1, max_val)

        return no

    # Índice passado como lista para ser mutável dentro da recursão
    return construir_util([0], float('-inf'), float('inf'))

# Exemplo de uso
preorder_seq = [8, 5, 1, 7, 10, 12]

raiz = construir_bst_preordem(preorder_seq)

print(raiz)
