def shell_sort(lista:list[int]) -> list[int]:
    gap = len(lista)//2
    while gap > 0:
        for i in range (0, gap, 1):
            if lista[i] > lista[i+gap]:
                aux = lista[i]
                lista[i] = lista[i+gap]
                lista[i+gap] = aux
            print(lista)
        gap -= 1
            
    return lista

listaDesordenada = [20, 9, 13, 16, 21, 32, 12, 1]
print(f"Lista desordenada: {listaDesordenada}")

listaOrdenada = shell_sort(listaDesordenada)
print(f"Lista ordenada: {listaOrdenada}")