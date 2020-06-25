#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 
# ## Download: http://github.com/dsacademybr

# # Versão da Linguagem Python
# from platform import python_version
# print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())

# ## Variáveis e Operadores 

# In[1]:


# Atribuindo o valor 1 à variável var_teste
var_teste = 1


# In[2]:


# Imprimindo o valor da variável
var_teste


# In[3]:


# Imprimindo o valor da variável
print(var_teste)


# In[5]:


# Não podemos utilizar uma variável que não foi definida. Veja a mensagem de erro.
my_var


# In[6]:


var_teste = 2


# In[7]:


var_teste


# In[8]:


type(var_teste)


# In[9]:


var_teste = 9.5


# In[10]:


type(var_teste)


# In[11]:


x = 1


# In[12]:


x


# ## Declaração Múltipla

# In[13]:


pessoa1, pessoa2, pessoa3 = "Maria", "José", "Tobias"


# In[14]:


pessoa1


# In[15]:


pessoa2


# In[16]:


pessoa3


# In[17]:


fruta1 = fruta2 = fruta3 = "Laranja"


# In[18]:


fruta1


# In[19]:


fruta2


# In[20]:


# Fique atento!!! Python é case-sensitive. Criamos a variável fruta2, mas não a variável Fruta2.
# Letras maiúsculas e minúsculas tem diferença no nome da variável.
Fruta2


# ## Pode-se usar letras, números e underline (mas não se pode começar com números)

# In[21]:


x1 = 50


# In[22]:


x1


# In[23]:


# Mensagem de erro, pois o Python não permite nomes de variáveis que iniciem com números
1x = 50


# ## Não se pode usar palavras reservadas como nome de variável
# 
# ## False      
# ## class      
# ## finally    
# ## is         
# ## return
# ## None       
# ## continue   
# ## for        
# ## lambda     
# ## try
# ## True       
# ## def        
# ## from       
# ## nonlocal   
# ## while
# ## and        
# ## del        
# ## global     
# ## not        
# ## with
# ## as         
# ## elif       
# ## if         
# ## or         
# ## yield
# ## assert     
# ## else       
# ## import     
# ## pass
# ## break      
# ## except     
# ## in         
# ## raise

# In[24]:


# Não podemos usar palavras reservadas como nome de variável
break = 1


# ## Variáveis atribuídas a outras variáveis e ordem dos operadores

# In[25]:


largura = 2


# In[26]:


altura = 4


# In[27]:


area = largura * altura


# In[28]:


area


# In[29]:


perimetro = 2 * largura + 2 * altura


# In[30]:


perimetro


# In[31]:


# A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2)  * altura


# In[32]:


perimetro


# ## Operações com variáveis

# In[33]:


idade1 = 25


# In[34]:


idade2 = 35


# In[35]:


idade1 + idade2


# In[36]:


idade2 - idade1


# In[37]:


idade2 * idade1


# In[38]:


idade2 / idade1


# In[39]:


idade2 % idade1


# ## Concatenação de Variáveis

# In[40]:


nome = "Steve"


# In[41]:


sobrenome = "Jobs"


# In[42]:


fullName = nome + " " + sobrenome


# In[43]:


fullName


# # Fim

# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>

# In[ ]:




