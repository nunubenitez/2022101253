from flask import Blueprint, request, jsonify
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
import os, signal
from time import sleep
import pandas as pd
from unipath import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
 
setest02 = Blueprint('setest02', __name__)

@setest02.route('/setest02', methods=['POST'])
def llamarServicioSet():
    global codigo, password
    ##try:
    codigo =request.json['codigo']
    password =request.json['password']
    inicializarVariables(codigo,password)
    
     
    salida = {'codRes': codRes, 'menRes': menRes}
    return jsonify({'ParmOut':salida})

def inicializarVariables(codigo,password):
    global codRes, menRes, driver, PID
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    # Configuración de las opciones de Chrome
    edge_options = Options()
    edge_options.add_argument("--start-maximized")  # Iniciar Chrome maximizado
    edge_options.add_argument('--ignore-certificate-errors')
    #chrome_options.add_argument("--test-type")
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    msedgedriver_path = 'C:/Users/neara/Desktop/python curso/clase 6/msedgedriver.exe'
    # Inicializa el servicio de ChromeDriver
    service = Service(msedgedriver_path)

    # Crea una instancia del navegador Chrome
    driver = webdriver.Edge(service=service, options=edge_options)
    driver.set_page_load_timeout(15)            
    try:
            driver.get('https://jaguarete.unida.edu.py/docente/Login')
            accesoSet(codigo,password)
    except TimeoutException:
            driver.close()
            driver.quit()
            print("No se pudo abrir la pagina jaguarete !!!")


def accesoSet(codigo,password):
    global menRes,codRes
    

    try:
        codigo = driver.find_element(By.ID, 'codigo')
        codigo.send_keys("2022101253")
        sleep(5)
        password = driver.find_element(By.ID, 'password')
        password.send_keys("Elwiwi26")
        sleep(5)
        login = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
        login.click()
        sleep(5)
        driver.close()
        driver.quit()
        
             
    except Exception as e:
        print("ERROR EN: login, intento driver.close() - driver.quit",str(e))
        driver.close()
        driver.quit()
        print("ERROR EN: login, termine driver.close() - driver.quit")