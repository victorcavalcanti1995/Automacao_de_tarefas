import pyautogui
import time

pyautogui.PAUSE = 0.5 # faz com que entre um comando e outro de uma pausa(evita encavalar os comandos caso necessário)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Entrar no sistema da empresa
# - abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
 # - entrar no site
pyautogui.write(link)
pyautogui.press("enter")
 # - fazer uma pausa maior para o site carregar (nesse momento especifico do código)
time.sleep(4)

# Passo 2: Fazer login
 # - clicar no campo de email
pyautogui.click(x=728, y=407)# a posição muda de acordo com a resolução em que o computador está rodando)
pyautogui.write("projetodev@gmail.com")
pyautogui.press("tab") # passa para o campo senha
pyautogui.write("12345")
pyautogui.press("tab") # passa para o botão
pyautogui.press("enter")
 # - fazer uma pausa maior pro site carregar
time.sleep(3) 

# Passo 3: Abrir a base de dados (importar o arquivo) (para  saber quais produtos cadastrar)
 # - pip install pandas openpyxl (o openpyxl permite o pandas a trabalhar com base de dados em excel se nessesário)
import pandas 
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: # esse código vai executar cada linha da tabela por causa do .index que significa indice se eu quise executar cada coluna da tabela seria .columns
    # Passo 4: Cadastrar produtos
    # código
    # pyautogui.press("tab")
    pyautogui.click(x=712, y=300)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca
    marca = str(tabela.loc[linha, "marca"]    )
    pyautogui.write(marca)
    pyautogui.press("tab")
    # tipo    
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    # preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # obs    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": # essa linha de código faz com que o NaN não seje escrito na obs, somente é escrito se tiver alguma informação
        pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar

    pyautogui.press("enter")

    # - voltar para o ínicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos.

