def pot (n: int, p: int) -> int:
    if p ==0:
        return 1

    return n * pot(n, p-1)

numero = int(input('Digite o número que deseja encontrar a sua pontencia: '))
potencia = int(input('Digite a potencia desejada: '))

resultado = pot(numero, potencia)

print(f"A potência de {potencia} na base {numero} é: {resultado}")
