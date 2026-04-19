op=1
while op !=0:

    print("Calculadora")
    print("1 - adição")
    print("2 - Multiplicação")
    print("3 - Subtação")
    print("4 - Divisão")
    print("0 - Sair ")

    op=int(input("Escolhar uma opção"))
    match op:
        case 1:
            n1=float(input("Informe um valor: "))
            n2=float(input("informe outro valor: "))
            result = n1+n2
            print(f"resultado: {result} ")
        case 2:
            n1=float(input("Informe um valor: "))
            n2=float(input("informe outro valor: "))
            result = n1*n2
            print(f"resultado: {result} ")
        case 3:
            n1=float(input("Informe um valor: "))
            n2=float(input("informe outro valor: "))
            result = n1-n2
            print(f"resultado: {result} ")
        case 4:
            n1=float(input("Informe um valor: "))
            n2=float(input("informe outro valor: "))
            result = n1/n2
            print(f"resultado: {result} ")

        case 0:  
            print("Encerrando.. ate a próxima")

        case _:
            print("Opção invalida")             
                    
