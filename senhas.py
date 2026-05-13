import random

senhas = {}
def avaliar_forca(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_simbolo = False
   

    for c in senha:
        if 'A' <= c <= 'Z':
            tem_maiuscula = True
        elif 'a' <= c <= 'z':
            tem_minuscula = True
        elif '0' <= c <= '9':
            tem_numero = True
        else:
            tem_simbolo = True

    pontos = tem_maiuscula + tem_minuscula + tem_numero + tem_simbolo

    if len(senha) < 6 or pontos <= 1:
        return "fraca"
    elif pontos == 2 or pontos == 3:
        return "média"
    else:
        return "forte"


def gerar_senha(tamanho):
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = "!@#$%&*()-_=+[]{};:,.?/"

    caracteres = letras + numeros + simbolos

    senha = ""
    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha


def cadastrar_senha():
    try:
        servico = input("Serviço: ").strip()

        if servico in senhas:
            print(" Serviço já existe!")
            return

        senha = input("Senha: ").strip()

        forca = avaliar_forca(senha)
        senhas[servico] = senha

        print(f" Cadastrada! Força: {forca}")

    except Exception as e:
        print("Erro:", e)


def listar_servicos():
    if not senhas:
        print("Nenhum serviço.")
        return

    for s in senhas:
        print("-", s)


def buscar_senha():
    try:
        servico = input("Serviço: ").strip()

        if servico in senhas:
            print("Senha:", senhas[servico])
        else:
            print(" Não encontrado.")

    except:
        print("Erro na busca.")


def gerar_senha_menu():
    try:
        tamanho = int(input("Tamanho: "))
        print("Senha gerada:", gerar_senha(tamanho))
    except:
        print("Entrada inválida.")


def avaliar_todas():
    if not senhas:
        print("Nenhuma senha cadastrada.")
        return

    for servico, senha in senhas.items():
        print(servico, "-", avaliar_forca(senha))


def exportar_relatorio():
    try:
        with open("relatorio.txt", "w", encoding="utf-8") as f:
            for servico, senha in senhas.items():
                forca = avaliar_forca(senha)
                f.write(f"{servico} | {senha} | {forca}\n")

        print(" Exportado com sucesso!")

    except Exception as e:
        print(" Erro ao exportar:", e)
while True:
    print("\n[1] Cadastrar")
    print("[2] Listar")
    print("[3] Buscar")
    print("[4] Gerar senha")
    print("[5] Avaliar todas")
    print("[6] Exportar")
    print("[7] Sair")

    try:
        op = int(input("Opção: "))

        if op == 1:
            cadastrar_senha()
        elif op == 2:
            listar_servicos()
        elif op == 3:
            buscar_senha()
        elif op == 4:
            gerar_senha_menu()
        elif op == 5:
            avaliar_todas()
        elif op == 6:
            exportar_relatorio()
        elif op == 7:
            break
        else:
            print(" Opção inválida.")

    except:
        print(" Digite um número válido.")