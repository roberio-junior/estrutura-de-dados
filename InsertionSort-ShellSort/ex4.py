def insertion(lista: list[tuple], indice: int,) -> list[tuple]:

    for i in range (indice, 0, - 1):

        if lista[i][2] == lista[i-1][2]:
            if lista[i][1] == lista[i-1][1]:
                if lista[i][0] == lista[i-1][0]:
                    break

                elif lista[i][0] < lista[i-1][0]:
                    aux = lista[i]
                    lista[i] = lista[i-1]
                    lista[i-1] = aux
                else:
                    break

            elif lista[i][1] < lista[i-1][1]:
                aux = lista[i]
                lista[i] = lista[i-1]
                lista[i-1] = aux
            else:
                break

        elif lista[i][2] < lista[i-1][2]:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
        else:
            break
            
    return lista

def insertion_sort(lista: list[tuple]) -> list[tuple]:
    for i in range (1, len(lista), 1):
        insertion(lista, i)
            
    return lista

lista_datas = [
    (1, 2, 2023),    # dias iguais
    (1, 5, 2024),

    (12, 3, 2024),   # meses iguais
    (25, 3, 2025),

    (10, 8, 2025),   # anos iguais
    (22, 10, 2025),

    (15, 4, 2026),   # dias e meses iguais
    (15, 4, 2027),

    (5, 7, 2023),    # meses e anos iguais
    (20, 7, 2023),
    (1, 7, 2023),
    (31, 7, 2023),

    (30, 9, 2024),   # dias e anos iguais
    (30, 12, 2024),

    (11, 11, 2022),  # datas totalmente iguais
    (11, 11, 2022),

    (2, 6, 2021),    # totalmente diferentes
    (19, 10, 2027)
]

print(f"Lista desordenada: {lista_datas}\n")

listaOrdenada = insertion_sort(lista_datas)
print(f"Lista ordenada: {listaOrdenada}")