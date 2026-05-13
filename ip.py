ips = {"192.168.1.1", "10.0.0.5", "172.16.0.3"}

def cabecalho():
    print()
    print("------------------- AGENDA DE IPS ----------------")
    print("Adicionar digite 1")
    print("Buscar digite 2")
    print("Remover digite 3")
    print("Listar digite 4")
    print("Atualizar digite 5")
    print("Sair digite 6")

# adicionar
def adicionar_ip():
    endereco = input("Digite o IP: ")
    if endereco in ips:
        print("IP já existe!")
    else:
        ips.add(endereco)
        print("IP adicionado com sucesso!")

# buscar
def buscar_ip():
    endereco = input("Digite o IP: ")
    if endereco in ips:
        print("IP encontrado:", endereco)
    else:
        print("IP não encontrado.")

# remover
def excluir_ip():
    endereco = input("Digite o IP: ")
    if endereco in ips:
        ips.remove(endereco)
        print("IP removido com sucesso!")
    else:
        print("IP não encontrado.")

# listar
def listar_ip():
    if ips:
        print("Lista de IPs:")
        for ip in ips:
            print(ip)
    else:
        print("Nenhum IP cadastrado.")

# atualizar
def atualizar_ip():
    endereco = input("Digite o IP que deseja alterar: ")
    
    if endereco in ips:
        novo_ip = input("Digite o novo IP: ")
        ips.remove(endereco)
        ips.add(novo_ip)
        print("IP atualizado com sucesso!")
    else:
        print("IP não encontrado.")


# menu
def menu():
    while True:
        cabecalho()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_ip()
        elif opcao == "2":
            buscar_ip()
        elif opcao == "3":
            excluir_ip()
        elif opcao == "4":
            listar_ip()
        elif opcao == "5":
            atualizar_ip()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()