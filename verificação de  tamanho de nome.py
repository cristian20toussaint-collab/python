print("Verificaçao de tamanho de nome")

nome = input("digite seu nome: ")
tamanho = len(nome)

if tamanho < 5:
    print("nome curto")
elif tamanho <= 10:
    print("nome medio")
else:
    print("nome longo")
