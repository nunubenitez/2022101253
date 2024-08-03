from flask import Blueprint,request,jsonify


login = Blueprint('Login',__name__)


@login.route('/login',methods=['POST'])

def llamarServicioSet():
    user=request.json.get('user')
    password=request.json.get('password')

    codRes,menRes,accion= inicializarVariables(user,password)

    salida={
        'codRes':codRes,
        'menRes':menRes,
        'usuario':user,
        'accion':accion,

    }

    return jsonify(salida)

def inicializarVariables(user,password):
    userlocal='nunu'
    passlocal='unida123'
    codRes='SIN_ERROR'
    menRes='ok'
  
    try:
        print("Verificar login")

        if password == passlocal and user == userlocal:
            print("Usuario y contrena ok")
            accion = "Success"

        else:
            print("Usuario o clave erronea")
            accion="Usuario o contrasenia incorrecta"
            codRes='ERROR'
            menRes='Credenciales incorrectas'

    except Exception as e:
        print("Erorr ",str(e))
        codRes='ERROR'
        menRes='Msg:'+str(e)
        accion="Error interno"

    return codRes,menRes,accion