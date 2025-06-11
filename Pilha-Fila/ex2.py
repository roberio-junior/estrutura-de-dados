def navegador():
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║ <   >   ⟳  🔒 https://www.navegador.com                   ⌄  x ║")
    print("╠════════════════════════════════════════════════════════════════╣")
    print("║                                                                ║")
    print("║                                                                ║")
    print("║                            Navegador                           ║")
    print("║                                                                ║")
    print("║               🔍[______________________________]               ║")
    print("║                                                                ║")
    print("║                                                                ║")
    print("║                                                                ║")
    print("║                                                                ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")

def resultado_pesquisa(pesquisa: str):
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║ ◄   ►   ⟳  🔒 https://www.navegador.com/search?q=exemplo       ║")
    print("╠════════════════════════════════════════════════════════════════╣")

    tamanho = len(pesquisa)
    largura = 54
    if tamanho < 54:
        print(f"║ Pesquisa:{pesquisa}" + " " * (largura - tamanho) + "║")
    else:
        reduzida = ""
        for i in range (50):
            reduzida += pesquisa[i]
        print(f"║ Pesquisa:{reduzida}..." + " ║")

    print("║────────────────────────────────────────────────────────────────║")
    print("║ Primeiro Resultado                                             ║")
    print("║ 🌐 https://www.siteexemplo.com/artigo                          ║")
    print("║ Este é um breve resumo do conteúdo apresentado neste site.     ║")
    print("║────────────────────────────────────────────────────────────────║")
    print("║ Outro resultado relevante                                      ║")
    print("║ 🌐 https://www.outroexemplo.org/tema                           ║")
    print("║ Uma descrição genérica sobre o conteúdo relacionado à pesquisa.║")
    print("║────────────────────────────────────────────────────────────────║")
    print("║ Mais informações                                               ║")
    print("║ 🌐 https://www.informacoes.com/pagina                          ║")
    print("║ Texto resumido com possíveis explicações ou exemplos práticos. ║")
    print("╚════════════════════════════════════════════════════════════════╝")

palavra = "Ian é indiano?"

navegador()

historico = []
atual = ["HOME"]
def menu():
    global historico
    while True:
        print("\n╔══════════════════════════════╗")
        print("║       MENU DO NAVEGADOR      ║")
        print("╠══════════════════════════════╣")
        print("║ 1. ? Pesquisar algo          ║")
        print("║ 2. < Voltar                  ║")
        print("║ 3. > Avançar                 ║")
        print("║ 0. x Sair                    ║")
        print("╚══════════════════════════════╝")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            busca = input('Pesquise algo:')
            historico = []
            atual.append(busca)
        elif escolha == "2":
            if len(atual) == 1:
                pass
            else:
                retorno = atual.pop()
                historico.append(retorno)
        elif escolha == "3":
            if len(historico) == 0:
                pass
            else:
                avanco = historico.pop()
                atual.append(avanco)
        elif escolha == "0":
            print("Encerrando Navegador...")
            break
        else:
            print("Opção inválida. Tente novamente.")

        if len(atual) == 1:
            navegador()
        else:
            pesquisa = atual.pop()
            atual.append(pesquisa)
            resultado_pesquisa(pesquisa)

menu()