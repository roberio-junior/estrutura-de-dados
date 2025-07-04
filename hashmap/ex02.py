texto = input("Informe o texto:")

# Transforma o texto em letras minúsculas e separa por palavras
palavras = texto.lower().split()

# Cria um dicionário para armazenar as frequências
frequencia = {}

# Conta as palavras
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Exibe o resultado
print("Frequência das palavras:")
for palavra, contagem in frequencia.items():
    print(f"{palavra}: {contagem}")
