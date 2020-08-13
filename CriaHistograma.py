#Metodos e funcoes Numpy
import numpy as np #importa numpy
import matplotlib.pyplot as plt

print(np.random.rand(10))#imprime valores aleatorios usando numpy com valores aleatorio de random
plt.show(plt.hist(np.random.rand(10)))#cria um histogram com plt do matpltolib com valores aleatorios(10 valores)
plt.show(plt.hist(np.random.randn(1000)))#cria histograma com dados normais com valores aleatorios randn
print("Imprime Matriz 3x3")
print(np.random.rand(3,3))
# = np.random.rand(30,30)
#plt.imshow(img,cmap=plt.cm.hot)
#plt.colorbar()
