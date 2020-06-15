from functools import reduce
#Cria uma lista
lista= [1,16,2,444,69,8,4,36,54,87]
print(lista)
#gera um for para imprimir a lista
#for i in lista:
 #   print(i)

#agora gerar um reduce para verificar o maior valor da lista sendo que o lambda ira para uma variavel
chlista = lambda a , b: a if (a > b) else b
type(chlista)
print("Valor maior:")
teste=reduce(chlista,lista)
print(teste)