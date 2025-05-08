def fib(n):
    if n < 3:
        return 1
    return fib(n-1)+fib(n-2)

numero = int(input('Digite qual a posição do número desejado na sequência de Fibonacci: '))

resultado = fib(numero)

print (resultado)
