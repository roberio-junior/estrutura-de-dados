from collections import deque  # Importa deque para usar como fila eficiente

def bfs_labirinto(labirinto, inicio, objetivo):
    linhas = len(labirinto)
    colunas = len(labirinto[0])

    # Movimentos possíveis: cima, baixo, esquerda, direita
    movimentos = [(-1,0), (1,0), (0,-1), (0,1)]

    # Matriz para marcar as posições já visitadas
    visitado = [[False]*colunas for _ in range(linhas)]

    fila = deque()  # Cria a fila para posições a explorar

    fila.append(inicio)               # Adiciona o ponto inicial na fila
    visitado[inicio[0]][inicio[1]] = True  # Marca o inicial como visitado

    while fila:
        x, y = fila.popleft()  # Remove a posição da frente da fila

        if (x, y) == objetivo:  # Verifica se chegou no objetivo
            print("Objetivo encontrado em:", (x, y))
            return True

        # Explora as posições vizinhas
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            # Verifica se a nova posição é válida dentro do labirinto
            if 0 <= nx < linhas and 0 <= ny < colunas:
                # Só avança se o espaço não for parede e não tiver sido visitado
                if labirinto[nx][ny] == 0 and not visitado[nx][ny]:
                    fila.append((nx, ny))         # Adiciona para explorar depois
                    visitado[nx][ny] = True       # Marca como visitado

    print("Objetivo não encontrado.")
    return False


# Exemplo de uso:
labirinto = [
    [0, 1, 0, 0, 0],  # 0 = caminho livre, 1 = parede
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

inicio = (0, 0)    # Ponto inicial (linha, coluna)
objetivo = (4, 4)  # Ponto final

bfs_labirinto(labirinto, inicio, objetivo)
