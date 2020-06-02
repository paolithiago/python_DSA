
import os
#Criacao de lista para armazenar resultados

os.system("cls")
lista =[]

#Funcao para layout de tela

def teclaenter():
    input("Tecle Enter para prosseguir.....")
def inicial():
    os.system('cls')
    print("********************************* Python Calculator*********************")
    print("Selecione o numero da operação digitada:")
    print("1. Soma\n2.Subtracao\n3.Multiplicação\n4.Divisao")
    print("************************************************************************")
#Chama funcao Tela
inicial()
#Acessar opções
opcao = int(input("Digite a opção desejada:"))
while (opcao >=1) and (opcao <=4):#while que verifica opcoes
    valor1 = int(input("Digite o primeiro valor:"))
    valor2 = int(input("Digite o segundo valor:"))
    if(opcao == 1 ):#if soma
        soma_lam = lambda valor1, valor2: valor1 + valor2 #expressão lambda
        print("Soma dos valores = ",soma_lam(valor1,valor2))#imprime soma
        lista.append(soma_lam(valor1, valor2))#armazazena soma
        teclaenter()
    elif(opcao == 2 ) :
        sub_lam = lambda valor1, valor2: valor1 - valor2
        print("Subtracao dos valores = ", sub_lam(valor1, valor2))
        lista.append(sub_lam(valor1, valor2))
        teclaenter()
    elif (opcao == 3):
        mult_lam = lambda valor1, valor2: valor1 * valor2
        print("Multiplicacao dos valores = ", mult_lam(valor1, valor2))
        lista.append(mult_lam(valor1, valor2))
        teclaenter()
    elif (opcao == 4):
        div_lam = lambda valor1, valor2: valor1 / valor2
        print("Subtracao dos valores = ", div_lam(valor1, valor2))
        lista.append(div_lam(valor1, valor2))
        teclaenter()
    inicial()
    opcao = int(input("Digite a opção desejada:"))
else:
    print("Opcao de saida - Fim!!")
    teclaenter()
os.system('cls')
print("Valores Armazenados")
print(lista)