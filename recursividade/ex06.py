def mdc(a: int, b: int) -> int:
    resto = a % b
    if resto == 0:
        return b
    return mdc(b, resto)

a = 5
b = 10
print(f"O MDC entre {a} e {b} é {mdc(a, b)}.")
