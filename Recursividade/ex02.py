def soma(n: int) -> int:
    if n == 1:
        return 1
    
    return n + soma(n-1)

numero = int(input('Digite um número N natural (maior que 0), para encontrar a soma dos seus primeiros N números naturais: '))

resultado = soma(numero)

print(f"A soma de todos os números de 1 até {numero} é: {resultado}")