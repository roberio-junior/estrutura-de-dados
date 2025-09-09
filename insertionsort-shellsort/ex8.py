def insertion(lista: list[str], indice: int) -> list[str]:
    for i in range(indice, 0, -1):
        if lista[i] < lista[i-1]:
            lista[i], lista[i-1] = lista[i-1], lista[i]
        else:
            break
    return lista

def insertion_sort(lista: list[str]) -> list[str]:
    for i in range(1, len(lista)):
        lista = insertion(lista, i)
    return lista

def string_for_list(palavra: str) -> list[str]:
    return list(palavra)

def anagrama(lista: list[str]):
    lista1 = string_for_list(lista[0])
    lista2 = string_for_list(lista[1])

    ordenada1 = insertion_sort(lista1)
    ordenada2 = insertion_sort(lista2)

    if ordenada1 == ordenada2:
        return print(f"As palavras {lista[0]} e {lista[1]} são anagramas.")
    else:
        return print(f"As palavras {lista[0]} e {lista[1]} não são anagramas.")
    
palavras = ["termo", "metro"]
anagrama(palavras)

palavras2 = ["casa", "caso"]
anagrama(palavras2)
