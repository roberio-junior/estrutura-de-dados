from datetime import datetime
def shell_sort(lista: list[str]) -> list[str]:
    n = len(lista)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):
            data1 = datetime.strptime(lista[i], "%d/%m/%Y")
            aux = lista[i]
            j = i

            while j >= gap and datetime.strptime(lista[j - gap], "%d/%m/%Y") > data1:
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = aux
        
        gap //= 2

    return lista

lista_datas = [
    "01/02/2023", "01/05/2024",
    "12/03/2024", "25/03/2025",
    "10/08/2025", "22/10/2025",
    "15/04/2026", "15/04/2027",
    "05/07/2023", "20/07/2023",
    "01/07/2023", "31/07/2023",
    "30/09/2024", "30/12/2024",
    "11/11/2022", "11/11/2022",
    "02/06/2021", "19/10/2027"
]

print(f"Lista desordenada: {lista_datas}\n")

listaOrdenada = shell_sort(lista_datas)
print(f"Lista ordenada: {listaOrdenada}")
