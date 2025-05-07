import time

def pot (n: int, p: int) -> int:
    if p == 1:
        return n
    return n * pot(n, p-1)

numero = int(input('Digite o número que deseja encontrar a sua pontencia: '))
potencia = int(input('Digite a potencia desejada: '))

inicio = time.time()
resultado = pot(numero, potencia)
final = time.time()

print(f"A potência de {potencia} na base {numero} é: {resultado}")
print(f"Tempo de execução: {final-inicio}")