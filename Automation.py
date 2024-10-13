import pandas as pd #imports the libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tabela = pd.read_csv("produtos.csv") #imports the csv file into a variable

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options) #keeps the web browser open after the automation process ends

driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #navigates to the selected website

login = driver.find_element(By.XPATH, '//*[@id="email"]') #finds and selects the desired field using its XPATH
login.send_keys("User") #writes 'user' at the selected field
login = driver.find_element(By.XPATH, '//*[@id="password"]')
login.send_keys("senha aqui")
driver.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()

for linha in tabela.index: #starts a for loop that repeats the commands for each row in the CSV table
    campo = driver.find_element(By.XPATH, '//*[@id="codigo"]')
    campo.send_keys(tabela.loc[linha, "codigo"])
    campo = driver.find_element(By.XPATH, '//*[@id="marca"]')
    campo.send_keys(tabela.loc[linha, "marca"])
    campo = driver.find_element(By.XPATH, '//*[@id="tipo"]')
    campo.send_keys(tabela.loc[linha, "tipo"])
    campo = driver.find_element(By.XPATH, '//*[@id="categoria"]')
    campo.send_keys(str(tabela.loc[linha, "categoria"]))
    campo = driver.find_element(By.XPATH, '//*[@id="preco_unitario"]')
    campo.send_keys(str(tabela.loc[linha, "preco_unitario"]))
    campo = driver.find_element(By.XPATH, '//*[@id="custo"]')
    campo.send_keys(str(tabela.loc[linha, "custo"]))
    if not pd.isna(tabela.loc[linha, "obs"]): #if the selected cell is not null, it writes the value in the selected field. If it is null, it presses the Tab key.
        campo = driver.find_element(By.XPATH, '//*[@id="obs"]')
        campo.send_keys(tabela.loc[linha, "obs"])
    driver.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()
