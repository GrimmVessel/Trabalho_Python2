 #input do texto
texto= input("insira uma palavra: ").lower()
#definir a quantidade de caracteres
palavras = texto.split()

# dicionário de contagem
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# ordenar por frequência (do maior para o menor)
ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

# exibir resultados
print("\nFrequência das palavras:")
for palavra, qtd in ordenado:
    print(f"{palavra}: {qtd}")

# destacar a mais usada
if ordenado:  # evita erro se o usuário não digitar nada
    mais_frequente = ordenado[0]
    print("\nPalavra mais usada:")
    print(f"{mais_frequente[0]} (aparece {mais_frequente[1]} vezes)")


