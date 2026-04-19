print("Validação de senha simples")

senha = input("digite uma senha: ")

if len(senha) >= 8:
    print("senha válida")
else:
    print("senha inválida (mínimo 8 caracteres)")
