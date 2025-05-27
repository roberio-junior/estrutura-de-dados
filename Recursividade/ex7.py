def digitos(numero: int) -> int:
    if numero < 10:
        return 1
    return 1 + digitos(numero // 10)

num = 1000
print(f"O número {num} possui {digitos(num)} dígitos.")
