#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[1]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Strings

# ### Criando uma String
# Para criar uma string em Python você pode usar aspas simples ou duplas. Por exemplo:

# In[2]:


# Uma única palavra
'Oi'


# In[3]:


# Uma frase
'Criando uma string em Python'


# In[4]:


# Podemos usar aspas duplas
"Podemos usar aspas duplas ou simples para strings em Python"


# In[5]:


# Você pode combinar aspas duplas e simples
"Testando strings em 'Python'"


# ### Imprimindo uma String

# In[6]:


print ('Testando Strings em Python')


# In[7]:


print ('Testando \nStrings \nem \nPython')


# In[1]:


print ('\n')


# In[ ]:





# In[ ]:



        


# ### Indexando Strings

# In[9]:


# Atribuindo uma string
s = 'Data Science Academy'


# In[10]:


print(s)


# In[11]:


# Primeiro elemento da string. 
s[0]


# In[12]:


s[1]


# In[13]:


s[2]


# Podemos usar um : para executar um slicing que faz a leitura de tudo até um ponto designado. Por exemplo:

# In[14]:


# Retorna todos os elementos da string, começando pela posição (lembre-se que Python começa a indexação pela posição 0),
# até o fim da string.
s[1:]


# In[15]:


# A string original permanece inalterada
s


# In[16]:


# Retorna tudo até a posição 3
s[:3]


# In[17]:


s[:]


# In[18]:


# Nós também podemos usar a indexação negativa e ler de trás para frente.
s[-1]


# In[19]:


# Retornar tudo, exceto a última letra
s[:-1]


# Nós também podemos usar a notação de índice e fatiar a string em pedaços específicos (o padrão é 1). Por exemplo, podemos usar dois pontos duas vezes em uma linha e, em seguida, um número que especifica a frequência para retornar elementos. Por exemplo:

# In[20]:


s[::1]


# In[25]:


s[::2]


# In[22]:


s[::-1]


# ### Propriedades de Strings

# In[23]:


s


# In[24]:


# Alterando um caracter
s[0] = 'x'


# In[26]:


# Concatenando strings
s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'


# In[27]:


s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'


# In[28]:


print(s)


# In[29]:


# Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'


# In[30]:


letra * 3


# ### Funções Built-in de Strings

# In[31]:


s


# In[32]:


# Upper Case 
s.upper()


# In[33]:


# Lower case
s.lower()


# In[34]:


# Dividir uma string por espaços em branco (padrão)
s.split()


# In[35]:


# Dividir uma string por um elemento específico
s.split('y')


# ### Funções String

# In[36]:


s = 'seja bem vindo ao universo de python'


# In[37]:


s.capitalize()


# In[38]:


s.count('a')


# In[39]:


s.find('p')


# In[40]:


s.center(20, 'z')


# In[41]:


s.isalnum()


# In[42]:


s.isalpha()


# In[43]:


s.islower()


# In[44]:


s.isspace()


# In[45]:


s.endswith('o')


# In[46]:


s.partition('!')


# ### Comparando Strings

# In[47]:


print("Python" == "R")


# In[48]:


print("Python" == "Python")


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
