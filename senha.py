#validador de senha tem que pedir uma senha ao usuaário  repetidamente usando while até que todos os critérios sejam feitos
#8 caracteres, 1 letra maiuscula, 1 letra minuscula, ao menos um número  e um cactere especial
def senha_valida (senha):    
    if len(senha) < 8:
        return "senha invalida"
    #conferir se tem tudo
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)
    return tem_maiuscula and tem_maiuscula and tem_numero and tem_minuscula and tem_especial

#while 
while True:
    senha = input("Insira sua senha: ")

    if senha_valida(senha):
        print("Senha válida! Cadastro concluído.")
        break
    else:
        print("Senha inválida! A senha deve ter:")
        print("- Pelo menos 8 caracteres")
        print("- Uma letra maiúscula")
        print("- Uma letra minúscula")
        print("- Um número")
        print("- Um caractere especial")
  



