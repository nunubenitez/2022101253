from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Ruta al archivo msedgedriver.exe
msedgedriver_path = 'C:/Users/neara/Desktop/python curso/clase 6/msedgedriver.exe'

# Configuración de opciones para Microsoft Edge
edge_options = Options()
edge_options.use_chromium = True  # Usar el nuevo Microsoft Edge basado en Chromium

# Crear el servicio
service = Service(executable_path=msedgedriver_path)

# Crear el controlador de Microsoft Edge
driver = webdriver.Edge(service=service, options=edge_options)

# Abrir una página web
driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
codigo = driver.find_element(By.ID, 'codigo')
codigo.send_keys("2022101253")
sleep(5)
password = driver.find_element(By.ID, 'password')
password.send_keys("Elwiwi26")
sleep(5)
login = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
login.click()

# Esperar un poco (por ejemplo, 10 segundos)
sleep(10)

# Cerrar el navegador
driver.quit()