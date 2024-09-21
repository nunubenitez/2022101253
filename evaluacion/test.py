from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Configuración de las opciones de Microsoft Edge
edge_options = Options()
edge_options.use_chromium = True  # Utiliza el nuevo Microsoft Edge basado en Chromium

# Ruta al Microsoft Edge WebDriver (ajusta la ruta según tu ubicación)
edgedriver_path = r'C:\Users\neara\Desktop\python curso\evaluacion\msedgedriver.exe'

# Inicializa el servicio de Microsoft Edge WebDriver
service = Service(edgedriver_path)

# Crea una instancia del navegador Microsoft Edge
driver = webdriver.Edge(service=service, options=edge_options)

# Abre la URL de ejemplo
driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')

# Ingresa tus credenciales
codigo = driver.find_element(By.ID, 'codigo')
codigo.send_keys("2022101253")
password = driver.find_element(By.ID, "password")
password.send_keys("unida")
login = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
login.click()

# Espera un poco para que puedas ver el resultado
sleep(10)

# Cierra el navegador
driver.quit()
