alunos1 = {
    "Ana": 7,
    "Bruno": 8,
    "Carlos": 6
}

alunos2 = {
    "Bruno": 7,
    "Ana": 9,
    "Daniel": 5
}

# Dicionário resultante
resultado = {}

for aluno, nota in alunos1.items():
    resultado[aluno] = nota  # adiciona aluno e nota do primeiro dicionário

for aluno, nota in alunos2.items():
    if aluno in resultado:
        resultado[aluno] += nota  # soma a nota se aluno já existir
    else:
        resultado[aluno] = nota  # adiciona novo aluno

print(resultado)
