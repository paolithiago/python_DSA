#!/usr/bin/env python
# coding: utf-8

# **** ATENÇÃO ****
# Caso você tenha problemas com acentos nos arquivos:
# 
# Primeiro, recomendamos a leitura do material sobre Formato Unicode, ao final do capítulo 4.
# 
# Uma forma de resolver esse problema, é abrir o arquivo em um editor de texto como o Sublime Text, clicar em File - Save with Encoding e então salvar com encoding UTF-8.
# 
# Outra opção é incluir o parâmetro encoding='utf8' ao abrir o arquivo para leitura ou escrita.

# Obs: Crie um arquivo txt, chamado arquivo1.txt no diretório "arquivos" na pasta onde está seu Jupyter Notebook, digite a frase: Python é uma linguagem poderosa! e salve o arquivo.

# In[1]:


#primeiro vamos abrir o arquivo,tem que colocar o caminho do arquivo, onde ele estiver, no nosso caso esta dentro do cap04 porem
#dentro de arquivos
arq1 = open("arquivos/arquivo1.txt","r")


# In[2]:


#agora vamos ler o arquivo usando print e read
#read - le o arquivo
print(arq1.read())


# In[3]:


#agora vamos contar a quantidade de caracteres do arquivo
#funcao tell
print(arq1.tell())


# In[4]:


#seek vai ate um determinado ponto do arquivo lembrando que indexação do python começa com 0. linha e coluna++Estudar melhor
print(arq1.seek(0,0))


# In[5]:


#podemos usar o read para imprimir caracteres, considerando o ponto onde o cursosr esta, no nosso caso esta noincio devido
#a funcção anterior estar em 0,0
print(arq1.read(10))


# In[6]:


############Gravaçao de arquivo###################
#Precisa abrir com w de write, escfever , depois fechar e abrir com r de read para ler o arquivo. 


# In[7]:


#abrindo arquivo para gravação
arq2 = open("arquivos/arquivo.txt","w")


# In[8]:


#se abrirmos arquivo com w nao podemos aplicar o w


# In[9]:


#escrever no aqruivo usando write
arq2.write("Novo texto digitado por paoli")


# In[10]:


#fechando o arquivo como escrita
arq2.close()


# In[3]:


#agora vo abrir para ler o aqruvio
arq2 = open("arquivos/arquivo.txt","r")


# In[12]:


#agora vamos ler o conteudo do arq2
print(arq2.read())


# In[13]:


###Podemos acrescentar conteudo usando apende a


# In[14]:


#abre arquivo com apende para acrescentar
arq2 = open("arquivos/arquivo.txt","a")


# In[15]:


#abre a funçao write para digitar o conteudo a acrescentar
arq2.write(". Inserindo mais conteudo Paoli")


# In[16]:


#fecha arquivo no modo a(acrescentar)
arq2.close()


# In[17]:


#Abre arquivo no modo read para ler
arq2 = open("arquivos/arquivo.txt","r")


# In[18]:


#imprimr arquivo com novo conteudo
print(arq2.read())


# In[19]:


#vai ate o primeiro ponto do arquivo
print(arq2.seek(0,0))


# In[20]:


#imrpimi arquvivo desde o ponto 0,0print(arq2.read())


# In[21]:


#### Permitir que o usuario defina o nome do arquivo depois abrir com w , colocar um texto fechar e abrir com r para ver arquivo
filename = input("Digite o nome do arquivo:")#input de string nao precisa covnverter


# In[22]:


filename = filename + ".txt"#concatena com extensao do arquivo


# In[23]:


arq3 = open(filename,"w")#abre o arquivo para escrever


# In[24]:


arq3.write("ola, inserindo mais texto")#escreve


# In[25]:


arq3.close()#fecha o arquivo


# In[26]:


arq3 = open(filename,"r")#abre arquivo para ler


# In[27]:


print(arq3.read())#imprimi o que esta no arquivo


# In[28]:


arq3.close()#fecha o arquivo


# In[29]:


#separado por linhas
#primeiro vamos abrir o arquivo,tem que colocar o caminho do arquivo, onde ele estiver, no nosso caso esta dentro do cap04 porem
#dentro de arquivos
arquivo = open("arquivos/salarios.csv","r")#abre o aruiqvo .csv


# In[30]:


#Dividindo o arquivo por lihha


# In[31]:


#faz a leitura e salva o conteudo no data
data = arquivo.read()


# In[32]:


#aqui divide o arquivo de acordo com argumento que no caso e o \n que e o entere, entao a cada linha divide
#split divide meu arquivo baseado em criterio, o\n e o enter, semre que econtroar o enter separa divide
rows = data.split("\n")


# In[33]:


print(rows)#imprime o resultadp, arquivos separados por linha, visualização nao e ideal, mas temos aqruivo separado por linnha


# In[34]:


#imprime arquivo
print(arquivo.read())


# In[35]:


#fazer a divisao por coluna:


# In[36]:


#abre o arquivo que coloca em uma variavel f
f=open('arquivos/salarios.csv','r')


# In[37]:


#faz a leitura do arquivo e coloca na variavel data
data = f.read()


# In[38]:


#faz o split por linhas 
rows = data.split('\n')


# In[39]:


#cria uma lista vazia(esta em colchete e lista)
full_data = []


# In[40]:


#percorre a linha usa split em cada linha, 
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)    


# In[41]:


print(full_data)#agora esta separado por linha , cada linha separada por virgula


# In[42]:


#contar linha , preciso entao fazer os processos de abrir um arquivo csv,como read, jogar este arquivo em uma variavel, 
#criar uma variavel data com arquivo lido. criar uma vairavel ros para fazer o split , criar uma lista, criar um for
# para ler todas as lihas do arquivo, dentro do ro criar uma variaevel para receber o valor quando encotnrar virugal
#jogar este valor na lista


# In[43]:


#abre arquivo para leitura
f = open('arquivos\salarios.csv','r')


# In[44]:


#gravar a leitura em um objeto data
data = f.read()


# In[45]:


#faz o split de acordo com enter
rows = data.split('\n')


# In[46]:


#cria uma lista vazia
lista = []


# In[47]:


#percorre todas a linhas com quebras por coluna e usa split em cada linha, vai dividir cada linha pelo criterio virgula, 
#sempre que encontra virgula faz a quebra, e usa append para colocar issio a lista.
for row in rows:
    split_row = row.split(',')
    lista.append(row.split)


# In[48]:


#faz count para cdalinha dentro do objeto lista faz o count somando cada linha e incrementando o contador
count = 0 #cria o count
for i in lista: #gera o for do tamanho da lista que foi gerada a partir do split de linnha com criterio virgula
    count = count +1 #faz a cota


# In[51]:


print (count)


# In[52]:


#no processo acima contei linhas agora o objetivo e contar as colunas


# In[53]:


f = open('arquivos\salarios.csv','r')#abri arquivo para leitrua
data = f.read()#grava a leitura em um obejto data
rows = data.split('\n')#faz split por linha
lista = []#cria lusta vazia


# In[54]:


#percorre cada linha do objeto de linhas
for row in rows:
    split_row = row.split(',')#separa por coluna
    lista.append(split_row)#coloca  valor que achou ate a virgula
    fisrt_row = lista[0]#contabiliza cada coluna , busca cada elemento o de cada lista, uma linha quantas colunas tem
                        
        


# In[55]:


count = 0 #percorre cada coluna do fisrt row e imcrementa. 
for row in fisrt_row:
    count = count +1 


# In[56]:


print(count)#imprime qtde de colunas


# In[62]:


#usando Panda
import pandas as pd


# In[63]:


file_name = "arquivos/binary.csv"#leitura do arquivo


# In[64]:


#leitura d arquivo para dentro do objeto usando o pd que e um objeto do panda
df = pd.read_csv(file_name)


# In[65]:


#agorra vamos imprimir as primeiras linhas cabeça do aqruvivo
df.head()


# In[66]:


###agora vamos usar o panda com o aqruivo salarios que e maior , tem mais colnas
import pandas as pd # importa funcoes panda
filename ="arquivos/salarios.csv" # importa o arquvio salarios e joga para a variavel filename
df2 = pd.read_csv(filename)#leitura do arquivo csv para dentro da variavel df2
df2.head()# le as primeiras linhas do arquivp


# In[67]:


#Manipulando aqrquivos txt
#processo - criar a string(pode concatenrar),importar os, criar um arquvio e abrir o arquivo jogando para uma variavel,fazer 
#um for para preencher o arquivo com a tring que criou. Fechar o arquivo como escrita, abrir o arquivo como leitura
#salvar o arquivo em uma variavel, fechar arquvi como leitura e imprimir variavel que recebeu arquvivo


# In[68]:


#primeiro vamos criar uma string e jogar para vairaveis usando concatenação . Usamos concatenaçao de duas formas
texto = "Gosto de buscar em meus sonhos a esperança em dias melhores, e para isso e preciso lutar para que os sonhos se tornem realidade"
texto +="\nva em busca"
texto = texto  + "\nnunca desista"

print(texto)
# In[69]:


# import os - pacote para manipular o sistema opercioanl , manipula arquivos, manipular diretorios, manipular SO
import os 


# In[70]:


#join do modulo path do pacote os, usando o open para abrir este arquvivo, caso o aruivo nao esteja criado, se o arquivo mao
#exisitr a linguagem cria.
arquivo = open(os.path.join('arquivos/cientista.txt'),'w')


# In[71]:


# agora que criei o arquvio preciso jogar o valor da variavel texto para este arquivo, usar o for
for palavra in texto.split():#percorrer a string ate achar um espaço, da as palavras
    arquivo.write(palavra +' ' )# a cada hora que o for achar espaço, coloca o texto de antes com espaço assim preenchedo


# In[72]:


arquivo.close()#fecha o arquivo para escrita


# In[73]:


#lendo o arquivo
arquivo = open('arquivos/cientista.txt','r')


# In[74]:


#salvando o arquivo lido em uma variavel
conteudo = arquivo.read()


# In[75]:


arquivo.close()


# In[76]:


print(conteudo)


# In[77]:


#usar o with com open
with open ('arquivos/cientista.txt') as arquivo:#abre o arquivo com with open e da nome arquvivo
    conteudo = arquivo.read()#dai atribui o conteudo a uma variavel


# In[78]:


print(len(conteudo))


# In[79]:


print(conteudo)


# In[80]:


# podemo ainda usar notações de de slice, que e escrever texto a partir de indices dentro da strig
#usar o with com open
with open ('arquivos/cientista.txt','w') as arquivo:#abre o arquivo com with open e da nome arquvivo
    arquivo.write(texto[:2])#escrevo dentro do comtando duas posições desde o incio - slice
    arquivo.write('\n')#pulo uma linha
    arquivo.write(texto[:17])#escrev dentro  cotando 17 posicoes


# In[81]:


arquivo = open('arquivos/cientista.txt','r')#abro o arquvivo para leitura


# In[82]:


conteudo = arquivo.read()#jogo o arquivo em uma variavel


# In[83]:


print(conteudo)#imprimo a varival com valor do aqruvio com as conifg de slice


# In[84]:


###################Trabalhando com arquivos csv####################
import csv


# In[85]:


with open('arquivos/numeros.csv','w') as arquvivo: #abre um arquivo para escrita
    writer = csv.writer(arquvivo) #funcao CSV WRITER para escrever no arquivo
    writer.writerow(('primeira','segunda','terceira'))#preenche primeira limha(indexo começa com zero)
    writer.writerow((3,2,3))#preenche a segunda linha
    writer.writerow((4,5,6))#preenche a terceira linha


# In[86]:


with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for i in leitor:
  #      print('Verifica',len(i))
        print(i)


# In[87]:


# converter o arquvi para lista
with open('arquivos/numeros.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)
print(dados)


# #CONVERTE O CONTEUDO DO ARQUVIVO PARA UMA LISTA , ISSO E IMPORTANTE POIS NO PYTHON CADA OBJETO POSSUI METODOS E
# #ATRIBUTOS PARA MANIPULAÇÃO. TALVEZ VC MANIPULANDO O ARQUVIO NÃO TENHA O METODO NECESSARIO PARA MANIPULA ,
# #DAI CONVERTENDO POR EXEMPLO EM UMA LISTA TERA.	
# #por exemplo podemos percorrer a lista com um for

# In[88]:


#for para percorrer a lsita que salvei do arquivo. Assim uso um metodo de percorer a lista com for
for i in dados:
    print(i)


# In[89]:


#outra opção - usar o for para percorre a lista começando de um indice da lista , no caso abaixo na posição 03[3:], lemnbrando
#que python tem idexação iniciando de 0
for i in dados [3:]:
    print(i)


# In[90]:


###########################Aqruivos JSON##########################################################
#Manipulando arquivos JSON -Que sao arquivos java script objetc notation - podem ser usadod em bigdata
dict = {
    'nome':'Thiago',
    'linguagem':'Python',
    'Similar':['c','modula3','lisp'],#aqui criei um valor para similar como lista
    'users':1000000
}


# In[91]:


#importando aqrquivos json
import json


# In[92]:


#converter um arquivo dicionario para um objeto json
json.dumps(dict)


# In[93]:


#criado um aqruvio em json ccom escrita
#Aqui fiz a criação do arquvivo dados.json modo write com nome arquivo e  atribui o valor do dicionario
#acima para o arquvio
with open('arquivos/dados.json','w') as arquivo:
    arquivo.write(json.dumps(dict))#atribui o valor do dicionario para o aruivo json


# In[94]:


print(dict)


# In[95]:


#leitura de arquivo json
with open('arquivos/dados.json','r') as arquivo:#le o arquvio
    texto = arquivo.read()#grava em texto
    data = json.loads(texto)#carrega 


# In[96]:


print(data)#imprime


# In[97]:


#como se trata de um dicionario podem acessar por xemplo o nome e temos o retorno:
print(data['nome'])


# In[98]:


# Imprimindo um arquivo Json copiado da internet
from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]


# In[99]:


#imprimndo as colunas
print ('Título: ', data['title'])
print ('URL: ', data['url'])
print ('Duração: ', data['duration'])
print ('Número de Visualizações: ', data['stats_number_of_plays'])


# In[100]:


#Copiandndo conteudos de um arquivo para outro
import os#usando pacotes os que manipula arquivos em sistema operacional
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'


# In[101]:


#faz a trnasição da copia do valor de arquvio dados.json para arquivos/json_data.txt ao mesmo tempo m,.1q| ~Ç~L \ 
with open ('arquivos/dados.json','r') as infile:
    text=infile.read()
    with open ('arquivos/json_data.txt','w') as outfile:
        outfile.write(text)


# In[102]:


with open ('arquivos/json_data.txt','r') as arquivo:
    texto = arquivo.read()#grava em texto
    data = json.loads(texto)#carrega 


# In[103]:


print(data)


# In[104]:


######################   MODULOS E PACOTES #######################


# In[105]:


#INICAR COM MATH - OPERAÇÕES MATEMATICAS


# In[106]:


import math


# In[107]:


dir(math)#mostra metodos e atributos


# In[108]:


#usando o metodo math coma funcao de raiz quadrada
math.sqrt(25)


# In[109]:


#importando apenas um dos metodos de math, este e melhor do que importar todo o modulo math, pois pega o que precisa
from math import sqrt


# In[110]:


sqrt(9)


# In[111]:


help(sqrt)#ajuda para o metodo


# In[112]:


#usando a funcao import


# In[113]:


#AGORA uma função que dentre valores gera um sirteio randomico
import random #importa modulo random
random.choice(['maca','banana','laranja'])


# In[114]:


#AGORA uma funcao que faz uma seleção randomico de valores dentro de um conjunto de valor


# In[115]:


random.sample(range(100),10)#gera uma lista de 10 valores do conjunto 0 a 100


# In[116]:


#AGORA um modulo estatisico pora operações esatitiscas


# In[117]:


import statistics#importar modulo estatistico
list=[]#cria uma lista vazia


# In[118]:


list = random.sample(range(100),10)#lista recebe valores aleatorios gerados pelo sample


# In[119]:


print(list)#imprime a lista com os valores aleatorios


# In[120]:


statistics.mean(list)#media


# In[121]:


statistics.median(list)#mediana


# In[122]:


#PACOTE DATE TIME


# In[123]:


import datetime#podemos usar varios modulos e funcoes


# In[124]:


agora = datetime.datetime.now()#cria o valor de agora  do modulo date time do pacote datetime que retorna a data corrente


# In[125]:


agora


# In[126]:


#Podemos construir uma data 


# In[127]:


t = datetime.time(7,25,16)#criamos uma hora


# In[128]:


print(t)


# In[129]:


#desta hora que criei atraves de algumas funcoes posso extrair valores . Ex hora
print('Hora:',t.hour)
print('Minuto:',t.minute)
print('Segundo:',t.second)


# In[130]:


#podemos extrair dados nao so da hora mas tb da data
hoje = datetime.datetime.today()
print(hoje)


# In[131]:


print('CTIME:',hoje.ctime())#imprime uma forma da data como dia , mes extenso, dia hora e ano
print('DAY:',hoje.day)
print('MONTH:',hoje.month)
print('YEAR:',hoje.year)


# In[132]:


data1 = datetime.date(2015,4,28)
data2 = datetime.date(2014,4,28)
print(data1)
print(data2)


# In[133]:


data1-data2


# In[6]:


print(d2)


# In[135]:


#Funcao MAP - Para exemplificar, criar duas funcoes
#1.	Criar uma função que converte uma temperatura recebida como parâmetro e retornar como fahreneit
#2.	Criar uma função que converte uma temperatura e retorna a a temperatura em celsius


# In[8]:


#funcao que recebe temperatura como parametro e retorna temperatura em Fahreneit
def farhen (t):
    return("O Valor retornado para Fahreneit é:",float(9/5)*t + 32)
#funcao que recebe temperatura como parametro e retorna temperatura em Celsius
def cel (t):
    return("O Valor retornado para Celsius é:",float(5/9)*(t - 32))


# In[9]:


#criar uma lista para armazenar alguns valores
temperaturas = [0,22.5,40,100]
print(temperaturas)


# In[10]:


#Agora usamos a função map onde recebe uma função como parâmetro e a sequencia de elementos, em que o map vai aplicar a 
#função a cada elemento da lsita de valores e vai retornar a lista com os valores,  porem o map retorna o interator, 
#dai precisamos converter o resultado de map para uma lista.
map(farhen,temperaturas)


# In[11]:


#explicando MAP com minhas paavras, criei um funcao que faz a conversao e criei um lista com alguns valores, ao inves de por exemplo 
#converter os valores usando for acessando cada elemento dalista, o MAP ja aplica a funcao para cada um dos valores e retorna
list(map(farhen,temperaturas))


# In[12]:


# para o exemplo acima nao precisaria fazer um loop porem poderia
for temp in map(farhen,temperaturas):# o loop vai percorre
    print(temp)


# In[13]:


#agora fazer um MAP com a lista temperaturas porem convertendo para Celsius
map(cel,temperaturas)


# In[14]:


#porem ainda no exemplo acima problemas com o retorno do MAP que e um interator, precisa de ser covnertido para lista
list(map(cel,temperaturas))


# In[15]:


#Agora vamos usar o MAP com a funcao lambda, lembrando que lambda recebe um argumento e retorna o valor nao precisa de bloco
#exemplo para refrescar lambda
pot = lambda x:x**2
pot(2)


# In[16]:


#Usando Lambda com MAP e a lista temperaturas
map(lambda x:float(9/5)*x + 32,temperaturas)


# In[17]:


#tivemos que usar o list por causa do interator
list(map(lambda x:float(9/5)*x + 32,temperaturas))


# In[18]:


#podemos usar o map para somar os valores de duas listas, exemplos listas a e b com valoes quero somar as duas
#antes do map possivelmente teria que criar um for para somar
la=[1,2,3,4]
lb=[11,12,13,14]


# In[19]:


#aqui usamos o labda recebendo os valores x,y e depois somando  sendo os argumentos, os valores das listas la e lb
map(lambda x,y:x+y,la,lb)


# In[20]:


#para imprimir precisamos usar a list por causa do interator
list(map(lambda x,y:x+y,la,lb))


# In[21]:


#podemos usar map com lambda para somar os valores por exemplo de tres listas
la=[1,2,3,4]
lb=[3,4,5,6]
lc=[7,8,9,10]


# In[22]:


map(lambda x,y,z:x+y+z,la,lb,lc)


# In[23]:


list(map(lambda x,y,z:x+y+z,la,lb,lc))


# In[24]:


#Funcao REDUCE  - PRECISA SER IMPORTADA DO PACOTE FUNCTOOLS
from functools import reduce


# In[25]:


#vamos criar uma lista simples
lista = [47,11,42,13]


# In[26]:


lista


# In[27]:


#agora criar uma funcao que soma dois valores que recebe dois parametros soma e retorna, veja que e uma funcao simples
def soma(a,b):
    x=a+b
    return(x)
soma(2,3)


# In[28]:


#agora posso aplicar nossa lista a funcao, isso, aplicando o reduce a funcao soma , soma todos valores da listqa
reduce(soma,lista)


# In[29]:


#Podemos tb executar um funcao lambda com reduce
reduce(lambda x,y:x+y,lista)


# In[30]:


#Cria uma lista com alguns valores e imprime para verificacao
lista= [1,16,2,4,69,8,4,36,54,87]
print(lista)


# In[31]:


#Chama Funcao Reduce do pacote functools
from functools import reduce


# In[32]:


#primeiro criado a função lambda com a compração do valor maior, caso seja imprime a senao impimre b, verifica com type o tipo
#e com a funcao reduce mostrou o maior valor****** So funcinou no Jupiter, no PyCharm
chlista = lambda a , b: a if (a > b) else b
type(chlista)
print("Valor maior:")
reduce(chlista,lista)


# In[33]:


####FUNCAO FILTER - Capaz de aplicar algum tipo de filtro, também recebe dois argumentos -> funções e sequencias,
#oferece maneira de filtrar elementos caso a função seja verdadeira. 
#primeiro criar uma funcao que verifica se o numero e par
#Abaixo a funcao recebe um argumento (numero) e verifica se e par ou nao

def ver_par (num):
    if num % 2 ==0:
        return True
    else:
        return False
ver_par(5)


# In[34]:


#criei uma lista qualquer , agora e chamar o filter jutno com esta lista para que verifique cada um dos valores da lista
#e filtre o que for par
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]


# In[35]:


lista


# In[36]:


# A funcao filter tb retorna interator assim precisa converter em lista
filter(ver_par,lista)


# In[37]:


#assim retornamos como lista so os valores que de fato sao pares de acrodo com a funcao ver_par
list(filter(ver_par,lista))


# In[38]:


#podemos usar uma experessão labda com filter
list(filter(lambda x:x%2==0,lista))


# In[39]:


#podemos usar outro filtro para lamvda, exemplo verificar qual valor maior que 11
list(filter(lambda x:x>8,lista))


# In[40]:


##############################List Comprehension###############################
#retorna x para cada valor de x dentro de um sequencia , como exemplo abaixo.
#Retornou uma lista composta por cada elemento em uma sequencia 

lst = [x for x in 'python']


# In[41]:


lst


# In[42]:


# Exemplo Paoli - a cada valor da lista que sera recebidaa pelo valor de x em um range de 0 a 11 soma-se com numero 2
teste = [x+2 for x in range(0,11)]


# In[43]:


teste


# In[44]:


#Mais um exemplo professor, fazer uma lista comprehension em que so salvara os valores pares
#foi adicionado um condicional if na list
lst1 = [x for x in range(11) if x % 2 == 0]


# In[45]:


lst1


# In[46]:


# consigo converter os valores de uma lista em celsius para fahreneit
cel = [0,10,20.1,34.5]
far = [float(9/5)*t + 32 for t in cel]


# In[47]:


far


# In[48]:


############################## ZIP ###############################
#criando duas lista
x=[1,2,3]
y=[4,5,6]


# In[49]:


#agora usei o zip para unir elementos das duas listas que sao criadas como tuplas, serão tuplas dentro de listas, porem
#como map e filter, a funcao retorna interator, necessitando converter para lista
zip(x,y)


# In[50]:


#converte em lista e exibe o resultado
list(zip(x,y))


# In[51]:


# veja que como foi conceituado o zip junta os registros porem segue a ordem da menor sequencia
list(zip('abcd','xy'))


# In[52]:


#criando duas novas listas, como ja conceituado o ZIP agrega de acordo com menor sequencia
a=[1,2,3]
b=[4,5,6,7,8]
list(zip(a,b))


# In[53]:


# podemos tb usar o zip para unir valores de dicionarios que vem entre chaves
d1 = {'a':2 , 'b':3}
d2 = {'c':5 , 'd':6}


# In[54]:


#aqui se da o valor agregado dos dois dicionarios como uma lista enviando indice
list(zip(d1,d2))


# In[55]:


#caso prefira por exemplo agregar o indice d1 com o valores d2:
list(zip(d1,d2.values()))


# In[56]:


#Agora criar um funcao para trocar os valores dos dicionarios
def trocavalores(d1,d2):
    dictemp = {}
    for dlkey,d2val in zip(d1,d2.values()):
        dictemp[dlkey] =d2val
    return dictemp

        
        


# In[57]:


trocavalores(d1,d2)


# In[58]:


############################## ENUMERATE ###############################
#Ao mesmo tempo que enumerate e simples ela e importante pois retorna lago muito importante --- o INDICE.
#O retorno da fucao enumerate e uma tupla contendo o índice  e o elemento.


# In[59]:


#Aqui criamos uma lista com as letras a, b e c e geramos a informaçao do indice com o enumerate(precisa usar o list ja que e 
#retorno interator)
seq = ['a','b','c']
list(enumerate(seq))


# In[61]:


#Podemos imprimir de forma diferente os valores da lista com índice usando enumerate 
for indice,valor in enumerate(seq):
    print(indice,valor)


# In[64]:


#Podemos imprimir tb parte dos valores de acordo com índices que posso selecionar por exemplo usando o
#for comparando se o índice e maior ou  igual a 2 para o for e imprime indice
#no exemplo abaixo o for vai ate enumerate da losta e se o indicie for maior igual a 2 para e retorna os valores do indice que
# o for rodou
for indice,valor in enumerate(seq):
    if indice >=2:
        break
    print(valor)


# In[65]:


#Mais uma lista em que vamos imorimir
lista = ['marketing','tecnologia','bi']


# In[67]:


#com o exemplo da lista acima vamos separar em indices
for i,item in enumerate(lista):
    print(i,item)


# In[77]:


#pomdemos tb extrair valores de indices em strings usando for, e enumerate
cont=0

for i,valor in enumerate('Python e uma ferramenta boa'):
    print(i,valor)
    cont +=1
print("Qtde de indices total da String - %s"%cont)


# In[88]:


#Aqui usei um texto extraido da internet em que uso for e enumerate para percorrer a string avaliando o valor dos indices e 
#valores, para cada analise de string roda cont para verificar a quantidade de strings
texto = 'A grosso modo a função print() serve para imprimir os argumentos passados a ela no terminal.Uma das grandes diferenças entre o Python 2 e 3 é que em Python 3 os argumentos passados para print() devem estar obrigatoriamente entre os parênteses.Para testarmos a função print() abra seu editor de textos ou IDE e crie o arquivo conversor.py com o seguinte código:'
cont=0
for i,valor in enumerate(texto):
    print(i,valor)
    cont +=1
print("Qtde de indices total da String - %s"%cont)


# In[89]:


texto = 'A grosso modo a função print() serve para imprimir os argumentos passados a ela no terminal.Uma das grandes diferenças entre o Python 2 e 3 é que em Python 3 os argumentos passados para print() devem estar obrigatoriamente entre os parênteses.Para testarmos a função print() abra seu editor de textos ou IDE e crie o arquivo conversor.py com o seguinte código:'
cont=0
for i,valor in enumerate(texto):
    if i >200:
        break
    print(i,valor)
    cont +=1
print("Qtde de indices total da String - %s"%cont)


# In[90]:


############################## ERROS E EXECESSOES ###############################
#abaixo e um erro de programação da linguagem, ja que faltou a aspas simples ao final do texto
print('Ola mundo)


# In[92]:


#agora vamos provocar um prblema de exceção.
#Criar uma funcao que recebe dois valores e divide um pelo outor e imprime resultado chama funcao com dois valores normais
#depois chamar a funcao com um valor comum dividindo por zero
def divisao(x,y):
    resultado = x/y
    print(resultado)


# In[93]:


divisao(4,2)


# In[94]:


#quando chamei a função e passei um dos argumentos seja 0 entao dentro regra matematica e errada. Este e um caso de exceção. Para
#isso professor informa que teria de tratar como exceção
divisao(4,0)


# In[1]:


#Tratamanento de erros excessões
#começamos com uma excessão simples em que tenta somar um valor inteiro com uma string
#Assim teremos um erro de Type Error 
#Neste exemplo precisamos usar um try - except
8 +'s'


# In[2]:


#Usando try tento fazer a operação e coloco o estado de exceção caso gere um erro:
    8 + 's'
except TypeError:
    print('Operação nao Permitida')


# In[25]:


#try except e else, tentar abri um arquivo e e gravar testamdo caso de uma erro de IOE iformar erro senao informa 
#gravado com sucesso
#vou criar o try com write
try:
    arq2 = open("arquivos/testandoerros.txt","w")
    arq2.write('Gravando no arquivo2 Paoli')
except IOError:
    print("Erro - arquivo nao encontrado ou nao pode ser salvo!!")
else:
    print("Arquivo gravado com sucesso!!!")
    arq2.close()


# In[26]:


#Aqui criei uma instrução para abrir o arquivo para leitura aops eu gravar uma mensagem:

arq2 = open("arquivos/testandoerros.txt","r")
print(arq2.read())


# In[36]:


arq2.close()


# In[ ]:


#Agora fiz uma tentativa de abrir um arquivo para LEITURA(R) que nao existe, assim o expcet informou erro.
#LEMBRANDO QUE PARA EU SALVAR EM UM ARUIVO EXISTETE POSSO USAR O W, POREM CASO O ARQUVIO NAO EXISTA, SE EU USAR O W CRIARA 
#UM NOVO ARQUIVO, ASSIM PARA TESTAR PRECISA TENTAR ACESSAR UM ARQUIVO EXISTENTE
try:
    arq2 = open("arquivos/testandoeros","r")
    arq2.write('Gravando no arquivo2 Paoli')
except IOError:
    print("Erro - arquivo nao encontrado ou nao pode ser salvo!!")
else:
    print("Arquivo gravado com sucesso!!!")
    arq2.close()


# In[3]:


#Agora com a insrução de erro acima inserio o Finaly , que mesmo com erro ou nao gera uma informação ou mensagem - indenpendente
#do erro
try:
    arq2 = open("arquivos/testandoeros","r")
    arq2.write('Gravando no arquivo2 Paoli')
except IOError:
    print("Erro - arquivo nao encontrado ou nao pode ser salvo!!")
else:
    print("Arquivo gravado com sucesso!!!")
    arq2.close()
finally:
    print("O Finally apresenta a mensagem independente de gerar erro ou nao")


# In[4]:


#Agora vamos criar uma funcao try para que o ususario receba um numero , converta em int e coloque excessao caso nao tenha digitação
def askint():
    try:
        val = int(input('Digite um valor'))
    except UnboundLocalError:
        print("Voce nao digitou um numero")
    finally:
        print("Obrigado")
    


# In[5]:


askint()


# In[6]:


#agora vou refazer o askint porem colocando dentro de except a opção novamente de digitação para o usuario, 
#Refzi porem so permite ao usuario digitar novamente 1 vez, caso seja digitado errado novamente vai paraa area de erro.
def askint():
    try:
        val = int(input('Digite um valor'))
    except:
        print("Voce nao digitou um numero")
        val = int(input('Digite um valor'))
    finally:
        print("Obrigado")
    


# In[1]:


askint()


# In[2]:


# para corrigir esta funcao , com loop wihle e cotinue no except
def askint():
    while True:
        try:
            val = int(input("Digite o valor"))
        except:
            print("Voce nao digitou valor")
            continue
        else:
            print("Obrigado!")
            break
        finally:
            print("Fim de execução")


# In[ ]:


askint()


# In[ ]:




