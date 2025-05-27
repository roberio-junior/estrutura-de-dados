# Implemente uma função recursiva que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente).
def palindromo(palavra: str):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return palindromo(palavra[1:-1])