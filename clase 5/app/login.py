from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login = Blueprint ('login', __name__)

DB_CONFIG = {
    'host': 'mysql-container-2',
    'user': 'unida',
    'password':'unida123',
    'database':'jaguarete'

}

@login.route('/login', methods=['POST'])
def llamarServiciosSet():
    user = request.json.get('user')
    password = request.json.get('password')

    codRes, menRes, usuario, accion = verificar_credenciales(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': usuario,
        'accion': accion
    }
    return jsonify(salida)

def verificar_credenciales (user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None
    
    try:
        print ("Verificar login")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        query = "SELECT username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))

        result = cursor.fetchone ()

        if result:
            usuario = result ['username']
            print ("Usuario y password OK")
            accion = "Sucess"
        else:
            print ("Usuario o password incorrecto")
            accion = "Usuario o password incorrecto"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
        cursor.close ()
        connection.close ()
    except Error as e:
        print ("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg:' + str(e)
        accion = "Error interno"
    return codRes, menRes, usuario, accion