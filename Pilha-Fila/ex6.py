class EditorTexto:
    def __init__(self):
        self.texto = "" # Armazena o texto atual do editor
        self.pilha = [] # Pilha que guarda as ações para desfazer

    def escrever(self, texto):
        self.texto += texto # Adiciona o texto digitado ao final do texto atual
        self.pilha.append(('escrever', texto)) # Registra a ação de escrever na pilha

    def apagar(self, n):
        if n > len(self.texto):
            n = len(self.texto) # Ajusta n para não apagar mais do que o texto atual
        apagado = self.texto[-n:] # Guarda os últimos n caracteres que serão apagados
        self.texto = self.texto[:-n] # Remove os últimos n caracteres do texto
        self.pilha.append(('apagar', apagado)) # Registra a ação de apagar na pilha

    def desfazer(self):
        if not self.pilha:
            print("Nada para desfazer.") # Se não tiver ação para desfazer, avisa e sai
            return
        acao, valor = self.pilha.pop() # Remove a última ação da pilha para desfazer

        if acao == 'escrever':
            # Para desfazer a escrita, remove o texto que foi adicionado
            self.texto = self.texto[:-len(valor)]
            print(f"Desfeito: removeu '{valor}'")
        else:  # ação 'apagar'
            # Para desfazer o apagado, adiciona o texto de volta
            self.texto += valor
            print(f"Desfeito: adicionou '{valor}' de volta")

    def mostrar(self):
        print(f"\nTexto: '{self.texto}'\n")  # Mostra o texto atual


def menu():
    editor = EditorTexto()  # Cria um editor

    while True:
        print("1 - Escrever")
        print("2 - Apagar")
        print("3 - Desfazer")
        print("4 - Mostrar texto")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == '1':
            t = input("Texto para escrever: ")
            editor.escrever(t)
        elif op == '2':
            n = int(input("Quantos caracteres apagar? "))
            editor.apagar(n)
        elif op == '3':
            editor.desfazer()
        elif op == '4':
            editor.mostrar()
        elif op == '0':
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
