frequencia = {}
texto = " "
while texto != "":
    texto = input("Informe o texto:")

    palavras = texto.lower().split()

# Conta as palavras
    for palavra in palavras:
        if palavra in frequencia.items():
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

# Exibe o resultado
print("Frequência das palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
