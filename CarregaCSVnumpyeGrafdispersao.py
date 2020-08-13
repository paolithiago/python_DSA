import os # importa biblioteca para acesso a sO
import numpy as np #importa biblioteca numpy
import matplotlib.pyplot as plt #importa bbiblioteca para gerar os graficos

filename = os.path.join("C:\PythonFundamentos\Cap08\iris.csv") #variavel filename recebe a planilha importa o arquivo
arquivo = np.loadtxt(filename, delimiter = ',', usecols = (0,1,2,3), skiprows = 1)#cria um array para receber o rarquiv
#completo porem sem a primeira coluna que e o cabeçalho
print(arquivo)#imprime o arquivo csv carregado
#abaixo variaveis recebem dois valores do aqruivo delimitados pelas colunas selecionadas em use cols
#depois gera grafico de dispersao de acordo com as colunas selecionadas 
var1,var2 = np.loadtxt(filename, delimiter = ',', usecols = (0,3), skiprows = 1,unpack=True)
plt.show(plt.plot(var1,var2,'o',markersize = 8,alpha=0.75))
