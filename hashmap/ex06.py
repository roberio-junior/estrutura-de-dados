# Dicionário com nomes dos alunos e suas listas de notas
alunos = {
    "Ana": [7, 8, 9, 10],
    "Bruno": [6, 7, 8, 5],
    "Carlos": [9, 10, 8, 7],
    "Daniel": [5, 6, 7, 8]
}

# Dicionário vazio para armazenar as médias dos alunos
medias = {}

# Calcula a média para cada aluno
for aluno, notas in alunos.items():
    soma = 0
    for nota in notas:
        soma += nota  # Soma todas as notas
    media = soma / 4  # Divide pelo número de notas (4)
    medias[aluno] = media  # Salva a média no dicionário medias

# Imprime a média de cada aluno
for aluno, media in medias.items():
    print(f"A média do aluno '{aluno}' é: {media}")
