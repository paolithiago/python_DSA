#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Tuplas

# In[2]:


# Criando uma tupla
tupla1 = ("Geografia", 23, "Elefantes")


# In[3]:


# Imprimindo a tupla
tupla1


# In[4]:


# Tuplas não suportam append()
tupla1.append("Chocolate")   


# In[5]:


# Tuplas não suportam delete de um item específico
del tupla1["Gatos"]  


# In[6]:


# Tuplas podem ter um único item
tupla1 = ("Chocolate")


# In[7]:


tupla1


# In[8]:


tupla1 = ("Geografia", 23, "Elefantes")


# In[9]:


tupla1[0]


# In[10]:


# Verificando o comprimento da tupla
len(tupla1)


# In[11]:


# Slicing, da mesma forma que se faz com listas
tupla1[1:]


# In[12]:


tupla1.index('Elefantes')


# In[13]:


# Tuplas não suportam atribuição de item
tupla1[1] = 21


# In[14]:


# Deletando a tupla
del tupla1


# In[15]:


tupla1


# In[16]:


# Criando uma tupla
t2 = ('A', 'B', 'C')


# In[17]:


t2


# In[18]:


# Tuplas não suportam atribuição de item
t2[0] = 'D'


# In[19]:


# Usando a função list() para converter uma tupla para lista
lista_t2 = list(t2)


# In[20]:


lista_t2


# In[21]:


lista_t2.append('D')


# In[22]:


# Usando a função tuple() para converter uma lista para tupla
t2 = tuple(lista_t2)


# In[23]:


t2


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
