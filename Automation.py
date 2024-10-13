import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tabela = pd.read_csv("produtos.csv")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)

driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

login = driver.find_element(By.XPATH, '//*[@id="email"]')
login.send_keys("Usuario aqui")
login = driver.find_element(By.XPATH, '//*[@id="password"]')
login.send_keys("Usuario aqui")
driver.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()

for linha in tabela.index:
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
    if not pd.isna(tabela.loc[linha, "obs"]):
        campo = driver.find_element(By.XPATH, '//*[@id="obs"]')
        campo.send_keys(tabela.loc[linha, "obs"])
    driver.find_element(By.XPATH, '//*[@id="pgtpy-botao"]').click()