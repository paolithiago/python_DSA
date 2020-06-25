#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Dicionários

# In[ ]:


# Isso é uma lista
estudantes_lst = ["Mateus", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25]   


# In[ ]:


estudantes_lst


# In[1]:


# Isso é um dicionário
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}


# In[2]:


estudantes_dict 


# In[3]:


estudantes_dict["Mateus"]


# In[4]:


estudantes_dict["Pedro"] = 23


# In[5]:


estudantes_dict["Pedro"]


# In[6]:


estudantes_dict["Tamires"]


# In[ ]:


estudantes_dict.clear()


# In[7]:


estudantes_dict


# In[8]:


del estudantes_dict


# In[9]:


estudantes_dict


# In[10]:


estudantes = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}


# In[11]:


estudantes


# In[12]:


len(estudantes)


# In[13]:


estudantes.keys()


# In[14]:


estudantes.values()


# In[15]:


estudantes.items()


# In[16]:


estudantes2 = {"Maria":27, "Erika":28, "Milton":26}


# In[17]:


estudantes2


# In[18]:


estudantes.update(estudantes2)


# In[19]:


estudantes


# In[20]:


dic1 = {}


# In[21]:


dic1


# In[22]:


dic1["key_one"] = 2


# In[23]:


print(dic1)


# In[24]:


dic1[10] = 5


# In[25]:


dic1


# In[26]:


dic1[8.2] = "Python"


# In[27]:


dic1


# In[28]:


dic1["teste"] = 5


# In[29]:


dic1


# In[30]:


dict1 = {}


# In[31]:


dict1


# In[32]:


dict1["teste"] = 10


# In[33]:


dict1["key"] = "teste"


# In[34]:


# Atenção, pois chave e valor podem ser iguais, mas representam coisas diferentes.
dict1


# In[35]:


dict2 = {}


# In[36]:


dict2["key1"] = "Big Data"


# In[37]:


dict2["key2"] = 10


# In[38]:


dict2["key3"] = 5.6


# In[39]:


dict2


# In[40]:


a = dict2["key1"]


# In[41]:


b = dict2["key2"]


# In[42]:


c = dict2["key3"]


# In[43]:


a, b, c


# In[44]:


# Dicionário de listas
dict3 = {'key1':1230,'key2':[22,453,73.4],'key3':['leite','maça','batata']}


# In[45]:


dict3


# In[46]:


dict3['key2']


# In[47]:


# Acessando um item da lista, dentro do dicionário
dict3['key3'][0].upper()


# In[48]:


# Operações com itens da lista, dentro do dicionário
var1 = dict3['key2'][0] - 2


# In[49]:


var1


# In[50]:


# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3['key2'][0] -= 2


# In[51]:


dict3


# ### Criando dicionários aninhados

# In[ ]:


# Criando dicionários aninhados
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}


# In[ ]:


dict_aninhado


# In[ ]:


dict_aninhado['key1']['key2_aninhada']['key3_aninhada']


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
