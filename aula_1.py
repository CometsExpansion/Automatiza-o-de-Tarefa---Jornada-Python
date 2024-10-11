import pandas as pd
import pyautogui as p
import time

p.PAUSE = 0.5
tabela = pd.read_csv('produtos.csv')


p.press('win')
p.write('opera')
p.press('enter')
time.sleep(1)   
p.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
p.press('enter')
time.sleep(5)
p.click(x=742, y=390)
p.write('exemplo@gmail.com')
p.press('tab')
p.write('exemplo')
p.press('enter')
p.press('tab')

for linha in tabela.index:
    var = str(tabela.loc[linha, 'codigo'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'marca'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'tipo'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'categoria'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'preco_unitario'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'custo'])
    p.write(var)
    p.press('tab')
    var = str(tabela.loc[linha, 'obs'])
    if var != 'nan':
        p.write(var)    
    p.press('tab')

    p.press('enter')
    p.scroll(5000)
    p.click(x=744, y=275)  