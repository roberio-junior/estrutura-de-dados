import time
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

numero = int(input('Digite o número que deseja encontrar o seu fatorial: '))

inicio = time.time()
resultado = fatorial(numero)
final = time.time()
print(f"O fatorial de {numero} é {resultado}")
print(final-inicio)