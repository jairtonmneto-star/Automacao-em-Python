#pyautogui.press
import pyautogui 
import time 
import pandas as pd
pyautogui.PAUSE=1 
pyautogui.press('win') 
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") 
pyautogui.press("enter") 
time.sleep(3) 
#print(pyautogui.position())
pyautogui.click(x=752,y=423)
pyautogui.write("jaula.@hotmail.com")#Gmail Inventado 
pyautogui.press("tab") 
pyautogui.write("Jaula1234") #Senha Tambem Inventado
pyautogui.press("tab")
pyautogui.press("enter")
tab=pd.read_csv("produtos.csv")
#print(tab)chrome
#for e intem para uma lista de itens por exemplo linha/tabela
#Cadastrar Todos os Produtos/.index e a lista com todos os indices da tabela para as linhas
for linha in tab.index:
    pyautogui.click(x=682,y=301)
    Codigo=tab.loc[linha,"codigo"]
    pyautogui.write(str(Codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tab.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tab.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tab.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tab.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tab.loc[linha,"custo"]))
    pyautogui.press("tab")
    obs=tab.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    #da Scroll para cima
    #pyautogui.scroll(5000)
