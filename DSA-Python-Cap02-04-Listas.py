#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Listas

# In[2]:


# Criando uma lista
listadomercado = ["ovos, farinha, leite, maças"]


# In[3]:


# Imprimindo a lista
print(listadomercado)


# In[4]:


# Criando outra lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]


# In[5]:


# Imprimindo a lista
print(listadomercado2)


# In[6]:


# Criando lista
lista3 = [12, 100, "Universidade"]


# In[7]:


# Imprimindo
print(lista3)


# In[8]:


lista3 = [12, 100, "Universidade"]


# In[9]:


# Atribuindo cada valor da lista a uma variável.
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]


# In[10]:


# Imprimindo as variáveis
print(item1, item2, item3)


# ### Atualizando um item da lista

# In[11]:


# Imprimindo um item da lista
listadomercado2[2]


# In[12]:


# Atualizando um item da lista
listadomercado2[2] = "chocolate"


# In[13]:


# Imprimindo lista alterada
listadomercado2


# ### Deletando um item da lista

# In[15]:


# Out of index. Não é possível deletar um item que não existe na lista
del listadomercado2[4]   


# In[16]:


# Deletando um item específico da lista
del listadomercado2[3]


# In[17]:


# Imprimindo o item com a lista alterada
listadomercado2


# ### Listas de listas (Listas aninhadas)
# Listas de listas são matrizes em Python

# In[18]:


# Criando uma lista de listas
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]


# In[19]:


# Imprimindo a lista
listas


# In[22]:


# Atribuindo um item da lista a uma variável
a = listas[0]


# In[23]:


a


# In[24]:


b = a[0]


# In[25]:


b


# In[26]:


list1 = listas[1]


# In[27]:


list1


# In[28]:


valor_1_0 = list1[0]


# In[29]:


valor_1_0


# In[30]:


valor_1_2 = list1[2]


# In[31]:


valor_1_2


# In[32]:


list2 = listas[2]


# In[33]:


list2


# In[34]:


valor_2_0 = list2[0]


# In[35]:


valor_2_0


# ### Operações com listas

# In[38]:


# Criando uma lista aninhada (lista de listas)
listas = [[1,2,3], [10,15,14], [10.1,8.7,2.3]]


# In[39]:


listas


# In[40]:


a


# In[41]:


b = listas[1][2]


# In[42]:


b


# In[43]:


c = listas[0][2] + 10


# In[44]:


c


# In[45]:


d = 10


# In[46]:


d


# In[47]:


e = d * listas[2][0]


# In[48]:


e


# ### Concatenando listas

# In[49]:


lista_s1 = [34, 32, 56]


# In[50]:


# Atribuindo à variável a, o primeiro valor da primeira lista
a = listas[0][0]


# In[51]:


lista_s1


# In[52]:


lista_s2 = [21, 90, 51]


# In[53]:


lista_s2


# In[54]:


# Concatenando listas
lista_total = lista_s1 + lista_s2


# In[55]:


lista_total


# ## Operador in

# In[56]:


# Criando uma lista
lista_teste_op = [100, 2, -5, 3.4]


# In[57]:


# Verificando se o valor 10 pertence a lista
print(10 in lista_teste_op)


# In[58]:


# Verificando se o valor 100 pertence a lista
print(100 in lista_teste_op)


# ## Funções Built-in

# In[59]:


# Função len() retorna o comprimento da lista
len(lista_teste_op)


# In[60]:


# Função max() retorna o valor máximo da lista
max(lista_teste_op)


# In[ ]:


# Função min() retorna o valor mínimo da lista
min(lista_teste_op)


# In[ ]:


# Criando uma lista
listadomercado2 = ["ovos", "farinha", "leite", "maças"]


# In[ ]:


# Adicionando um item à lista
listadomercado2.append("carne")


# In[ ]:


listadomercado2


# In[ ]:


listadomercado2.append("carne")


# In[ ]:


listadomercado2


# In[ ]:


listadomercado2.count("carne")


# In[ ]:


# Criando uma lista vazia
a = []


# In[ ]:


print(a)


# In[ ]:


type(a)


# In[ ]:


a.append(10)


# In[ ]:


a


# In[ ]:


a.append(50)


# In[ ]:


a


# In[ ]:


old_list = [1,2,5,10]


# In[ ]:


new_list = []


# In[ ]:


# Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)


# In[ ]:


new_list


# In[ ]:


c = [20,30]


# In[ ]:


c.append(60)


# In[ ]:


c.append(70)


# In[ ]:


c


# In[ ]:


c.count(20)


# In[ ]:


cidades = ['Recife', 'Manaus', 'Salvador']
cidades.extend(['Fortaleza', 'Palmas'])
print (cidades)


# In[ ]:


cidades.index('Salvador')


# Lembre-se: em Python o índice começa por 0!

# In[ ]:


cidades.index('Rio de Janeiro')


# In[ ]:


cidades


# In[ ]:


cidades.insert(2, 110)


# In[ ]:


cidades


# In[ ]:


# Remove um item da lista
cidades.remove(110)


# In[ ]:


cidades


# In[ ]:


# Reverte a lista
cidades.reverse()


# In[ ]:


# Imprime a lista
cidades


# In[ ]:


x = [3, 4, 2, 1]


# In[ ]:


x


# In[ ]:


# Ordena a lista
x.sort()


# In[ ]:


x


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
