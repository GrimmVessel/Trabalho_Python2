alunos = [
    ("Carlos", 8.5),
    ("Ana", 9.2),
    ("Bruno", 6.0),
    ("Diana", 7.8),
    ("Eduardo", 4.5),
]

# inicialização
maior_nota = alunos[0][1]
menor_nota = alunos[0][1]
aluno_maior = alunos[0][0]
aluno_menor = alunos[0][0]
soma = 0

# percorre a lista
for nome, nota in alunos:
    soma += nota

    if nota > maior_nota:
        maior_nota = nota
        aluno_maior = nome

    if nota < menor_nota:
        menor_nota = nota
        aluno_menor = nome

# média
media = soma / len(alunos)

# alunos acima da média
acima_media = []
for nome, nota in alunos:
    if nota > media:
        acima_media.append(nome)

# resultados
print("Maior nota:", maior_nota, "-", aluno_maior)
print("Menor nota:", menor_nota, "-", aluno_menor)
print("Média da turma:", round(media, 2))
print("Alunos acima da média:", acima_media)