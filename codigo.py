#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado
#pyautogui.hotkey -> apertar um conjunto de teclas (CTRL C, CTRL V, ALT Tab)
#print(pyautogui.KEYBOARD_KEYS)
#site: https://pyautogui.readthedocs.io/en/latest/
#para instalar: pip install pyautogui

# passo a passo do projeto

#1. Abrir o sistema da empresa
   # https://dlp.hashtagtreinamentos.com/python/intensivao/login
   
import time
import pyautogui

pyautogui.PAUSE = 0.5


# Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

#2. Fazer login
pyautogui.click(x=865, y=513)
pyautogui.write("exemplo@gmail.com")

pyautogui.press("tab") #passou para o campo de senha
pyautogui.write("0055112")

pyautogui.press("tab") #passou para o campo de login
pyautogui.press("enter")

#3. Abrir/Importar a base de dados de produtos para cadastrar  
#pip install pandas numpy openpyxl
import pandas as pd
tabela = pd.read_csv("produtos.csv")

print(tabela)
   
#4. Cadastrar um produto

for linha in tabela.index:
   
   codigo = str(tabela.loc[linha, "codigo"])

   #clicar no campo do codigo do produto
   pyautogui.click(x=805, y=370)
   
   #preencher o codigo
   pyautogui.write(codigo)
      #passar pro proximo campo
   pyautogui.press("tab")

   #marca
   pyautogui.write(str(tabela.loc[linha, "marca"]))
   #passar pro proximo campo
   pyautogui.press("tab")

   #tipo
   pyautogui.write(str(tabela.loc[linha, "tipo"]))
   #passar pro proximo campo
   pyautogui.press("tab")

   #categoria
   pyautogui.write(str(tabela.loc[linha, "categoria"]))
   #passar pro proximo campo
   pyautogui.press("tab")

   #preço
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   #passar pro proximo campo
   pyautogui.press("tab")

   #custo
   pyautogui.write(str(tabela.loc[linha, "custo"]))
   #passar pro proximo campo
   pyautogui.press("tab")

   #obs
   obs = str(tabela.loc[linha, "obs"])
   if obs != "nan":
      pyautogui.write(obs)
   #passar pro proximo campo
   pyautogui.press("tab")

   #apertar o botão
   pyautogui.press("enter")
   pyautogui.scroll(5000)
   
#5. Repetir isso tudo até acabar  a lista de produtos