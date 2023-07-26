import pandas as pd
import time
import pyautogui

# Setando o intervalo padrão entre as ações do pyautogui
pyautogui.PAUSE = 0.5
tempo_espera = 2

# Abrindo o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrando no site
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(url)
pyautogui.press("enter")
time.sleep(tempo_espera)

# Logando
email = "email@hotmail.com"
senha = "JCQmpBg$$5EN08Oj0Lb4Ae"

pyautogui.click(x=940, y=396) # clicando o primeiro campo do email. OBS: Mudar as coordenadas caso a resolução do monitor é diferente
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(tempo_espera)

# Cadastrando os dados
percurso = "F:\Progetti\Visual Studio Code\Python\Jornada Python\Python Power Up\produtos.csv"

tabela = pd.read_csv(percurso)

for linha in tabela.index:
    # Voltar ao início da tela e clicar no primeiro campo para inserir os dados
    pyautogui.press("pageup")
    pyautogui.click(x=831, y=271)
    
    for coluna in tabela.columns:
        if coluna == "obs":
            if not pd.isna(tabela.loc[linha, coluna]): pyautogui.write(str(tabela.loc[linha, coluna]))
            break
        
        pyautogui.write(str(tabela.loc[linha, coluna]))
        pyautogui.press("tab")
        
    pyautogui.press("tab")
    pyautogui.press("enter")