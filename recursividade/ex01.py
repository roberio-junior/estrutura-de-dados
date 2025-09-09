def fatorial(n: int) -> int:
    if n == 1:
        return 1
    return n * fatorial(n-1)

numero = int(input('Digite o número que deseja encontrar o seu fatorial: '))

resultado = fatorial(numero)

print(f"O fatorial de {numero} é {resultado}")
