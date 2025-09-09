def imprimir_reverso(vetor: list, indice: int) -> list:
    if indice < 0:
        return []
    
    return [vetor[indice]] + imprimir_reverso(vetor, indice - 1)

meu_vetor = [10, 20, 30, 40, 50]

print(imprimir_reverso(meu_vetor, len(meu_vetor) - 1))