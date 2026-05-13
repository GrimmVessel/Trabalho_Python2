vogal= (" a","e","i","o","u")  
consoante= ("b","c","d","f","g","h","j","k","l","m","n","p","q","r",
"s","t","v","w","x","y","z")
           
#frase
frase= input("insira uma frase:").lower()
#definir o que é uma frase
contador_v= 0
contador_c= 0
for i in frase :
    if i in  vogal:
        contador_v+=1
    if i in consoante:
        contador_c+=1

print(f'numero de vogais é: {contador_v}')
print(f'numero de consoantes é:{contador_c}')