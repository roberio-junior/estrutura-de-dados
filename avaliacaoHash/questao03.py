livro = {}
sumario = {}
while True:
    texto = input("Informe o conteúdo da página('FIM' para terminar o livro):")
    texto = texto.lower() 

    if texto == "fim":
        break

    pagina = int(input("PAG "))
    livro[pagina] = texto

    palavras = texto.lower().split()

    for palavra in palavras:
        if palavra not in sumario:
            sumario[palavra] = pagina
        else:
            sumario[palavra] += pagina

    print(sumario)
            





