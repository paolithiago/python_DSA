#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#criar um programa que receba idade como 18 e nome bob e colocar um if se idade maior que 13 e nome = bob imprime ok bob pode vir
#senao, nao pode entrar


# In[14]:


idade=18
nome="bob"
if idade>  13:
    if nome == "bob":
        print("oi, bob")
    else:
        print("nao, voce nao e o bob")
    


# In[15]:


#AND posso alterar o if aninhado por uma condiççao logica and, que so ira para opão verdadeira se as duas condiçoes forem verdadeiras


# In[24]:


idade = 18
nome = "bob"
if idade > 13 and nome == "bob":
    print("voce e o bob")
else:
    print("ou voce nao e bob ou vc nao tem mais que 13 anos")


# In[25]:


#OR - se uma das condições for verdadeira ja entra na instrução do if. So entra no else se todas condições forem falsas


# In[27]:


idade = 11
nome="bobo"
if (idade > 13) or (nome == "bob"):
    print("Ok vc e o bob")
else:
    print("vo nao e bob e nao tem mais que 13 anos")


# In[ ]:


#Elif evita de colocar if aninhado. Por exemplo, quero chegar os dias da semana, se for segunda –tal, 
#se for terça – tal, se for quarta – tal. Ao invés de usar um monte de if usa o elif.


# In[34]:


#Agenda Oi paoli
#1 - Segunda
#2 - Terca
#3 - Quarta
#4 - Quinta
#5 - Sexta
dia = int(input("Digite o dia da semana a analisar na Agenda:"))
if (dia == 1):
    print("Segunda - Reuniao PSR")
elif (dia == 2):
    print("Terça - Reuniao Spoke On line")
elif (dia == 3):
    print("Quarta - Preparação Material Reuniao de Resultado")
elif (dia == 4):
    print("Quinta - Reuniao Equipe HDM")
elif (dia == 5):
    print("Sexta - Reuniao Spoke Off line")
    
else:
    print("Fim de semana")


# In[ ]:


#façamos um programa que receba matéria e nota, coloque através do input em uma variave, e com operador logico 
#verifique se a matéria e geografia e a nota for maior que 70 , assim imprime aprovado senão reprovados


# In[44]:


materia = input("Digite a materia: ")
nota = float(input("Digite a nota: "))

if (materia == "geografia") and (nota > 70):
    print("Aprovado!!!")
else:
    print("Reprovado!!!")
    


# In[ ]:


#Para exemplificar, pediu que adicionasse mais uma variável e comparar se a disciplina for igual a geografia, 
#valor da nota for maior que 50 e semestre diferente de 1 , imprimir a disciplina e a nota:


# In[46]:


materia = input("Digite a materia:")
nota = input("Digite a nota:")
semestre = input("Digite o semestre:")

if (materia == "geografia") and (nota > "50") and (int(semestre) !=1):
    print("Voce esta aprovado na materia: %s com media de: %r"%(materia,nota))
else:
    print("Voce esta reprovado !!")


# In[ ]:


#######################LOOP For - repetir o comando com numer determinado de vezes#######################
#abre e fecha parenteses e tupla
#abre e fecha colchete e lista
#abre e fecha chave e dicionario


# In[ ]:


#Primeiro criar uma tupla e imprimi um loop for para imprimir todos os valores:


# In[48]:


tp = (2,3,6)
for i in tp:
    print(i)


# In[50]:


#imprimir uma lista de informações com for
listamercado = ["alface","cenora","azeiton"]
for i in listamercado:
    print(i)


# In[51]:


#Range – traz um range de valores em que o contador vai trabalhar. Range cria uma sequencia de valores
for cont in range(0,6):
    print(cont)
    


# In[52]:


#criar um loop for para verificar se os números da sequencia são pares ou não, no caso ira imprimir o que for par.
#Vamos utilizar valores da lista que criaremos  de 1 a 10.
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    if i % 2 ==0:
        print(i)


# In[54]:


#criar um for com incremento - por exemplo de 0 a 101 pulando de 2 em 2 com range:
for i in range(0,50,2):
    print(i)


# In[ ]:


#Loop For aninhado - Nomalmente usado para preencher matriz


# In[12]:


#Primeito loop externo . Segundo loop interno.  Para cada item do conjunt de item executa outra operação
for i in range(0,5):
    print("mat %r \n"%i)
    for a in range(0,5):
        print(a)


# In[28]:


#fazer um for para operar valores da lista no loop. usar uma variavel global soma e uma variavel interna double_i - a medida que o for
#roda a variavel double i recebe valor da lista no for * 2 e a variavel soma recebe soma + double i:

lista = [32,53,85,10,15,17,19]
soma=0
for i in lista:
    double_i = i*2
    soma += double_i
print(soma)


# In[25]:


#Loop de lista dentro de lista
Lista = [[1,2,3],[3,4,5,6],[6,7,8,9]]
for i in Lista:
    print(i)
print(Lista[0])
print(Lista[1])


# In[27]:


#Agora vamos contar valores dentro de uma lista com for. Exemplo – Conte os valores da lista [1,2,5,93,7,8,6,7]
#preciso fazer com  for porem preciso de uma variavel dentro do for para ser o contador - incializar ela fora
lista2 = [1,2,5,93,7,8,6,7]
cont = 0

for i in lista2:
    cont += 1
print(cont)


# In[31]:


#agora em uma lista com mais valores por indice, contar as colunas
lst = [[1,2,3],[3,4,5,6],[6,7,8,9]]
primeira = lst[0]
cont = 0
for colum in primeira:
    cont = cont +1
print(cont)


# In[38]:


#Podemos cria uma lista e buscar através do for  procurar valores dentor da lista e caso acha imprime, segue a lista
#Lista3 = [1,1,1,1,2,3,4,5,6,7,1,1,1,] –buscar o numero 1. No algoritimo abaixo ainda inclui um cont antes da instrução if 
#para contar todas posições do vetor para que ao impimir me informar a posição exata onde o numero 1 esta
Lista3 = [1,1,1,1,2,3,4,5,6,7,1,1,1,]
cont = 0
for n in Lista3:
    cont += 1 
    if n ==1:
        print("Loczalizado valor buscado -->1 na posicao: %r"%cont)


# In[43]:


#usando dicionario dic={"k1":"python";"k2":"java"}. Primeiro listas as chaves do dicionario(k1 e k2)
dic={"k1":"python","k2":"java"}
for i in dic:
    print(i)


# In[45]:


#usando dicionario dic={"k1":"python";"k2":"java"}. Agora listando chave e valores
dic2={"k1":"python","k2":"java"}
for k,v in dic.items():
    print(k,v)


# In[ ]:


############################loop While##########################


# In[3]:


#imprimir valores de 0 a 9 com while

cont = 0
while cont < 10:
    print(cont)
    cont +=1


# In[6]:


#imprimir de 0 9 informando que o valor... ainda e menor que 10 e ao final infromar fim do loop while
cou_n = 0
while cou_n  < 10:
    print("O valor :%r ainda e menor que 10"%cou_n)
    cou_n +=1
else:
    print("\n\nFim do loop!!!")
    


# In[9]:


#break e pass - interromper loop while
counter = 0
while counter <100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter +=1


# In[10]:


#continue axuilia pulando uma interação exemplo pular um string de uma palavra. aqui a palavra toda
for j in 'python':
    print(j)


# In[11]:


#continue axuilia pulando uma interação exemplo pular um string de uma palavra. aqui com o continue considerei que se a 
#letra for igual a y continua no laço for, nao imprime
for j in 'python':
    if j =='y':
        continue
    print(j)


# In[20]:


#verificar se os numeros sao primos de 2 a 6
for i in range (2,7):
    j=2
    cont=0
    while j<i:
        if i %  j == 0:# faz a a analise do valor didivido
            cont =1#se for igual a zero o mod cont receb 1 para separar se e primo
            j=j+1 #incrementa para depois sair do loop(verifica )
        else:
            j=j+1
    if cont == 0:
        print(str(i)+"Primo")
        cont = 0
    else:
        cont = 0


# In[ ]:


#############################################Range##############################################


# In[1]:


#imprimir numeros pares de 50 a 100
for i in range(50,101,2):
    print(i)


# In[2]:


#range que omite os passos considera de 1 em 1
for i in range(3,6):
    print(i)


# In[3]:


#podemos usar valores negativos com litas inversas -0 a -20
for i in range(0,-20,-2):
    print(i)


# In[12]:


#podemos aplicar range quando temos comprimento do objeto,posso criar uma lista atribuir a uma variavel o tamanho da lista
#usar len e depois fazer um for para ver a lsita de 0 a te o tamnha extraido do len

lista = ['galo','porco','peixe','raposa']#cria uma lista
lista_tamanho = len(lista) #atribui a uma variavel o tamanho da lista usando o len
print(lista_tamanho)#so para verificar, imprime oqtde de elementos da lista
for i in range(0,lista_tamanho): # for que comça do 0 e vai ate o tamanho da lista tirada pelo len
    print(lista[i])#imprime a lista na posição de acordo com  loop fo


# In[ ]:


################   Metdodos #####################


# In[4]:


#Priemiro exemplo, criar uma lista e inserir um valor novo
list=[1,2,3,-1,10]
list.append(10)
print(list)


# In[5]:


list.count(10)


# In[10]:


help(list.count)


# In[13]:


a="isso e uma string"
print(a.split())


# In[ ]:


###########################  Funções #######################


# In[ ]:


#Não precisa copiar o código toda vez que precisar da instrução.


# In[3]:


#Criando a dfinicao da funcaofuncao mais simple, usa , def, nome da funcao,abre e fecha parentese. 
#Colocar os dois pontos, e dentro do bloco precisa identar
def primeirafunc():
    print("hello")


# In[4]:


primeirafunc() #chama a funcao 


# In[8]:


#funcao com parametros - Aqui criei a funcao
def primeirafunc(nome):
    print("Oi, Sr(a)%s"%nome)


# In[9]:


primeirafunc("Paoli") #aqui chamei a funcao passando o parametor PaoliCap3.ipynb


# In[12]:


#criando um funcao com for dentro
def funLeitura():
    for i in range(1,5):
        print(i)
    


# In[13]:


funLeitura()


# In[14]:


#criar uma função para somar dois numeros
def somanum(val1,val2):
    print("Primeiro numero:" + str(val1))
    print("Primeiro numero:" + str(val2))
    print("O Resultado e :",val1+val2  )
    


# In[16]:


somanum(100,282)


# In[17]:


#variaveis locais e variaveis globais(as localis so funcionam dentro de funções)
varglobal = 10
def multiply(x,y):
    varglobal = x*y
    print(varglobal)


# In[18]:


#exemplo de aplicacao de variavel local vou chamar a funcação que tem umva variavael loval dentro da global
multiply(5,5)


# In[19]:


#exemplo de apliccacao de varivaell global que embira esteja um variavel local com mesmo nome, a varivel global que e vista
#pelo programa
print(varglobal)


# In[ ]:


################funções built in ####################


# In[21]:


################funções conversão ####################

valor = int(input("Digite um valor:"))
if valor >14:
    print("vc tem mais de 14")
else:
    print("Voce tem menos de 14")


# In[14]:


#######Funcoes dentro de funcoes - criar uma funçao que receb um texto e faz a split- separa por palavras.agr
def splittext(text):#criei uma função chamada splittext
    return text.split(" ")#que recebe um argumento e retorna o split considerando o espaço para criar a lista


# In[15]:


texto = "Thiago Paoli"


# In[16]:


print(splittext(texto))


# In[25]:


##################### entrada nas funções com varios argumentos ####################
def printvarios(arg1,*vartuple):
    print("O parametro foi :%s"%arg1)#aqui criei uma instruçao que imprime um valor de um argumento
    for i in vartuple:
        print("O parametro foi :%s"%i)


# In[26]:


printvarios("paoli")


# In[28]:


printvarios("agua","biscoito","uva passas","ovo","manteiga")


# In[ ]:


######### Expressoes Lambda ###########################


# In[2]:


#antes de crciar lambda vamos simplofar funcçoes com def
def potencia(pot):#cria a funcao potencia que recebe o argumento pot
    result = pot ** #eleva a potencia 2 - veja que tem variavel local result
    return result #retorna o resultado da potencia


# In[4]:


potencia(5)#chama a funcao e passa o valor 5 com resultado de 25


# In[5]:


#usar a funcao com somente duas linhas de codigo - Fizemos a operação sem variavel
def potencia(pot):#cria a funcao potencia que recebe o argumento pot
    return pot**2 #ja retorna o valor pot fazendo o calulo de potencia


# In[6]:


potencia(2)


# In[7]:


#usar a funcao com somente duas linhas de codigo - Fizemos a operação sem variavel
def potencia(pot):return pot**2 #cria a funcao potencia que recebe o argumento pot#ja retorna o valor pot fazendo o calulo de potencia


# In[8]:


potencia(3)


# In[9]:


#cria uma variavel que recebe a expressão lamda onde o argumento num1 fica como calculo dentro da expressao
pot = lambda num1:num1**2


# In[10]:


pot(2)


# In[2]:


#mais um exemplo de expressao lambda - uma variavel que recebe uma expressão lambda para verificar se valor e par
verifica =lambda x: x % 2 ==0


# In[4]:


verifica(3)


# In[9]:


#mais um exemplo de lambda, que verifica string e retorna o valor da posicao 0
ver_string = lambda x:x[0]


# In[10]:


ver_string('Paoli')


# In[11]:


#fazer uma soma usando lambda ,recebendo dois argumentos
soma_lam = lambda x,y: x+y


# In[12]:


soma_lam(2,3)


# In[ ]:




