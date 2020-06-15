import os
def farhen (t):
    return("O Valor retornado para Fahreneit é:",float(9/5)*t + 32)

def cel (t):
    return("O Valor retornado para Celsius é:",float(5/9)*(t - 32))

def teclaenter():
    input("Tecle Enter para prosseguir.....")
os.system("cls")
print("***** Conversor Temperaturas******")
op = int(input("Opcao 1 -Celsius para Farheneit\nOpcao 2 - Fahreneit para Celsius\nOpcao 0 - Sair\n"))
while (op != 0):
    if (op ==1):
        print("***** Conversor Temperaturas******")
        t = float(input("Digite o valor a converter para Fahreneit:"))
        print(farhen(t))
        teclaenter()
    elif(op==2):
        print("***** Conversor Temperaturas******")
        t = float(input("Digite o valor a converter para Celsius:"))
        print(cel(t))
        teclaenter()
    else:
        print("Opção errada")
        teclaenter()

    os.system("cls")
    print("***** Conversor Temperaturas******")
    op = int(input("Opcao 1 -Celsius para Farheneit\nOpcao 2 - Fahreneit para Celsius\nOpcao 0- Sair\n"))
else:
    print("Opcao de saida - Fim!!")
    teclaenter()
