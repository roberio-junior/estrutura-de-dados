# Escreva uma função recursiva que imprima todos os números de n até 1.
def imprimir_decrescente(n: int) -> str:
    if n == 1:
        return "1"
    return f"{n}," + f" {imprimir_decrescente(n - 1)}"

numero = 10
resultado = imprimir_decrescente(numero)

print(f"Números de {numero} até 1 (ordem decrescente):")
print(resultado)
