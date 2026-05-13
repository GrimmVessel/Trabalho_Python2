logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

contagem_niveis = {"INFO": 0, "WARNING": 0, "ERROR": 0}
erros_por_ip = {}
logs_processados = []
logs_invalidos = 0

for log in logs:
    try:
        partes = log.split("] ")

        nivel = partes[1].strip("[")
        resto = partes[2]

        mensagem, ip_parte = resto.split(" - IP: ")
        ip = ip_parte.strip()

        # Atualiza contagem de níveis
        if nivel in contagem_niveis:
            contagem_niveis[nivel] += 1
        else:
            raise ValueError("Nível desconhecido")

        # Conta erros por IP
        if nivel == "ERROR":
            erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1

        # Guarda log estruturado
        logs_processados.append({
            "nivel": nivel,
            "ip": ip,
            "mensagem": mensagem
        })

    except Exception:
        logs_invalidos += 1

# Descobrir IP com mais erros
ip_mais_erros = None
if erros_por_ip:
    ip_mais_erros = max(erros_por_ip, key=erros_por_ip.get)

# Relatório
print("=== RELATÓRIO DE LOGS ===\n")

print("Eventos por nível:")
for nivel, qtd in contagem_niveis.items():
    print(f"- {nivel}: {qtd}")

print("\nErros por IP:")
for ip, qtd in erros_por_ip.items():
    print(f"- {ip}: {qtd}")

print("\nIP com mais erros:")
if ip_mais_erros:
    print(f"- {ip_mais_erros} ({erros_por_ip[ip_mais_erros]} erros)")
else:
    print("- Nenhum erro encontrado")

print(f"\nLogs inválidos ignorados: {logs_invalidos}")