import pandas as pd
import time
import pyautogui


pyautogui.PAUSE = 0.5

# Abrindo o chrome e entrando no site
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# logando
pyautogui.click(x=940, y=396)
pyautogui.write("email@hotmail.com")
pyautogui.press("tab")
pyautogui.write("JCQmpBg$$5EN08Oj0Lb4Ae")
pyautogui.press("tab")
pyautogui.press("enter")

#cadastrando os dados
tabela = pd.read_csv("F:\Progetti\Visual Studio Code\Python\Jornada Python\Python Power Up\produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=831, y=271)
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter")
