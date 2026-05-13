#: Crie um programa que compare dois sets: um com IPs que acessaram o servidor e outro com uma blacklist de IPs maliciosos.
#exiba: quais IPs maliciosos foram detectados (interseção), quais IPs são seguros (diferença),
#IPs da blacklist não apareceram (diferença inversa) e 
#o total de IPs únicos considerando ambas as listas (união). Exiba os resultados formatados.
acessos = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
           "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}
blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172",  "23.94.5.100", "104.244.72.115"}

ips_suspeitos= acessos & blacklist
ips_certos= acessos - blacklist
ips_errados= blacklist - acessos
todos= blacklist|acessos

print("IPs maliciosos detectados:")
for i in ips_suspeitos:
    print (i)
print("\nIPs seguros:")
for i in ips_certos:
    print (i)

print("\nIPs da blacklist que não apareceram:")
for i in ips_errados:
    print( i)




print("\nTotal de IPs únicos:", len(todos))

