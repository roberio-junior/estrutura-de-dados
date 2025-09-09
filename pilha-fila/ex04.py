def inverter_string(texto):
    pilha = []  # Criamos a pilha vazia

    # Empilhamos cada caractere da string
    for caractere in texto:
        pilha.append(caractere)

    invertida = ""  # Inicio da string invertida

    # Desempilha os caracteres e adiciona na string
    while pilha:
        invertida += pilha.pop()

    return invertida

# Exemplo de uso:
entrada = input("Digite uma palavra ou frase: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
