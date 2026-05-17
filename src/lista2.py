lista = list(range(1,11))

pares=[]
for numero in lista:
    if numero %2==0:
        pares.append(numero)
  
print("lista original;", lista)
print("Numeros pares;",pares)  
