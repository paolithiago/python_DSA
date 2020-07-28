import sqlite3
import random
import datetime
import matplotlib.pyplot as plt

# Criando uma conexão
conn = sqlite3.connect('dsa.db')

# Criando um cursor - o cursor auxilia a percorrer toda tabela. Toda instrução deve ser utilizado o cursor com execute
c = conn.cursor()


# Função para criar uma tabela
#Lembrando que quando
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, ' \
              'prod_name TEXT, valor REAL)')


# Função para inserir uma linha
def data_insert():
    c.execute("INSERT INTO produtos VALUES(1,'2018-02-02 12:33', 'Teclado', 130 )")
    conn.commit()
    c.close()
    conn.close()

# Usando variáveis para inserir dados
def data_insert_while(data,nomeprod,valor):
    new_date = data
    new_prod_name = nomeprod
    new_valor = valor
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)",
              (new_date, new_prod_name, new_valor))
    conn.commit()

# Usando variáveis para inserir dados
def data_insert_var():
    #newcod = random.randrange(50,100)
    new_date = datetime.datetime.now()
    new_prod_name = 'monitor'
    new_valor = random.randrange(50, 100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)",
              (new_date, new_prod_name, new_valor))
    conn.commit()


# Leitura de dados
def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)


# Leitura de registros específicos
def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in c.fetchall():
        print(linha)

    # Leitura de colunas específicos


def leitura_colunas():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])

    # Update


def atualiza_dados():
    c.execute("UPDATE produtos SET valor = 70.00 WHERE valor > 80.0")
    conn.commit()


# Delete
def remove_dados():
    c.execute("DELETE FROM produtos WHERE prod_name = 'monitor'")
    conn.commit()


# Gerar gráfico com os dados no banco de dados
def dados_grafico():
    c.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids, valores)
    plt.show()
def cadastro_geral():
        data = input("Digite a data:")
        nome = input("Digite o Nome:")
        valor = int(input("Digite o valor:"))
        data_insert_while(data, nome, valor)
        cadastro = int(input("Deseja cadastrar?"))

#create_table()
#data_insert()
#for i in range(1,10):
#    data_insert_var()
#leitura_todos_dados()

print("Programa de cadastro e Consulta de Banco de dados")
print("*************************************************\n")
flag = int(input("Digita a opção - 1-Cadastro - 2 Consulta - 0 Sair:\n"))
while flag !=0:
    if (flag == 1):
        cadastro = int(input("Deseja Cadastrar?"))
        while cadastro == 1:
            print("Cadastro")
            cadastro_geral()
            cadastro = int(input("Deseja Cadastrar?"))
        else:
            print("Voltando ao Menu")
            flag = int(input("Digita a opção - 1-Cadastro - 2 Consulta - 0 Sair"))

    elif (flag == 2):
        print(("Consulta"))
        leitura_todos_dados()
        #break
        flag = int(input("Digita a opção - 1-Cadastro - 2 Consulta - 0 Sair"))
    else:
        print("Fim")
        break
else:
    print("Fim")
