#!/usr/bin/env python
# coding: utf-8

# # <font color='blue'>Data Science Academy - Python Fundamentos - Capítulo 5</font>
# 
# ## Download: http://github.com/dsacademybr

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios

# In[2]:


# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        


# In[3]:


roc1 = Rocket(1,2)#instancia a classe com nome roc1


# In[4]:


roc1.x #chama atributo x


# In[5]:


roc1.y #chama atributo y


# In[6]:


roc1.move_rocket() # aciona o metodo comum move_rocket onde duas vairaveisinternas _incrment sao incializadas com  0 e 1
# e assim incrementam de acordo com as variavieis incializadas ao instnciar o objeto e depois soma


# In[8]:


roc1.print_rocket()#imprime os valores dos atributos incrementados


# In[ ]:


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


# In[18]:


class Pessoa():#sempre lembrar que o nome da classe deve ser maiusuculo. Cria a Classe pessoa
    def __init__(self,nome,cidade,telefone,email):#metodo par aincializar os atributos de um objeto
        print("Construtor OK!")#Imprime uma mensagem informando sobre a construção do objeto de acordo com atributos
        self.nome = nome#instancia o atributo nome do objeto
        self.cidade = cidade#instancia o atributo nome do objeto
        self.telefone = telefone#instancia o atributo nome do objeto
        self.email = email#instancia o atributo nome do objeto
        
    def cidadebeaga(self):#criei um metodo comum que verifica se a cidade do objeto e BH, se for imprime voce e de BH
        if self.cidade == "BH":
            return "Voce e de Belo Horixonte"
        else:
            return "voce nao e de bh"
        
    
    def __str__(self):#este metodo especial retorna um texto string
        return "O funcionario é: %s, que mora na cidade:%s, com telefone:%s, e email:%s"%(self.nome,self.cidade, self.telefone,self.email)
    


# In[19]:


thiago = Pessoa("thiago paoli","BH",3134522177,"tpacheco25@hotmail.com")#instancia o objeto chamado de thiago a classe pessoas
#com os atrobutos passados como parametro


# In[20]:


str(thiago)#chamei o metodo str para o objeto thiago


# In[21]:


thiago.cidadebeaga()#aqui chamei o metodo comum se confere se a instancia cidade do objeto criado e BH se for retorna que
# e de belo horizonte, senao retorna outro texto


# In[23]:


pessoa2 = Pessoa("Joao","SP",1134558978,"joao@gmail.com")#aqui criei um novo objeto chamado pessoa 2 passando os parametros


# In[30]:


#imprimi os atributos
print(pessoa2.nome)
print(pessoa2.cidade)
print(pessoa2.telefone)
print(pessoa2.email)


# In[31]:


str(pessoa2)#chama o metodo especial str que retorna uma string


# In[33]:


pessoa2.cidadebeaga()#chamei novamente o metodo para conferir SE A NOVA pessoa e ou nao de BH


# In[ ]:


# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.


# In[42]:


class Smartphone(object):#aqui criei a classe smartphone como objeto, que tem somente um metodo , sendo ele especial constru
#tor, que recebe os atributos tamanho e interface e imprime a informação de construtor ok
    def __init__(self,tamanho,interface):#inicializa e recebe os parametros
        print("Construtor OK!!!") #informa construção ok
        self.tamanho = tamanho#recebe via parametro o tamanha como atributo do objeto
        self.interface = interface #recebe via parametro a interface como atributo do objeto
    


# In[49]:


class MP3Layer(Smartphone):#cria a classe MP3 com um init apontando para a classe smartphone
    def __init__(self,capacidade,tamanho,interface):#cria o incializador do MP3
        Smartphone.__init__(self,tamanho,interface)#cria herança com a classe smartphone herdando todos atributos
        self.capacidade = capacidade#criei um atributo espeficico da sub classe
        print("Objeto Criado")


# In[50]:


tel1 = MP3Layer("mega","Grande","plus")#instanciei o tel 1 como objeto da subclasse mp3layer que herda dados da classe
#smartphone


# ### FIM

# In[52]:


#Veja que mesmo instanciando a subclasee MP3Layer, consegui acesso ao atributo da classe smartphone,herdada para sub
print(tel1.tamanho)
print(tel1.capacidade)


# ### Obrigado - Data Science Academy - <a href="http://facebook.com/dsacademybr">facebook.com/dsacademybr</a>
