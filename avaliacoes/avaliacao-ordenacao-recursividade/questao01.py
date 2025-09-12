def palindromo(palavra: str):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    
    return palindromo(palavra[1:-1])

def insertion(lista: list[int], indice: int,) -> list[int]:
    for i in range (indice, 0, - 1):
        if lista[i] < lista[i-1]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[int]) -> list[int]:
    for i in range (1, len(lista), 1):
        lista = insertion(lista, i)
            
    return lista

entrada = ["ana", "casa", "arara", "luz", "radar"]
lista_ordenada = insertion_sort(entrada)

palindromos = []
for i in range (len(entrada)):
    if palindromo(entrada[i]) == True:
        palindromos.append(entrada[i])

lista_ordenada = insertion_sort(entrada)

print(f"Lista ordenada: {lista_ordenada}")
print(f"Palíndromos identificados:{palindromos}")