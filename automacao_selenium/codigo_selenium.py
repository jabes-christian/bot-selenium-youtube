from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# abrir o navegador 
navegador = webdriver.Chrome()

# acessar o site do YouTube
navegador.get("https://www.youtube.com/")
navegador.maximize_window()
time.sleep(2)

# localizar o campo de pesquisa e digitar o termo
campo_pesquisar = navegador.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
campo_pesquisar.send_keys("John Frusciante")
time.sleep(2)

# clicar no botão da lupa
botao_lupa = navegador.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/button')
botao_lupa.click()
time.sleep(3)

# esperar os resultados aparecerem e pegar o primeiro vídeo
primeiro_video = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.XPATH, '(//a[@id="video-title"])[1]'))
)

# rolar até ele
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", primeiro_video)
time.sleep(1)

# aguardar que esteja clicável
WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, '(//a[@id="video-title"])[1]'))
)

# clicar no vídeo
primeiro_video.click()

# esperar um pouco para o vídeo carregar
time.sleep(30)
navegador.quit()