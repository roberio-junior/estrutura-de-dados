def soma_vetores(lista: list ) -> int:
    if len(lista) == 1:
        return lista[0]
    return lista[0] + soma_vetores(lista[1:])

vetor = [3, 5, 7, 2, 8]

resultado = soma_vetores(vetor)

print(f"A soma dos elementos do vetor {vetor} é {resultado}.")