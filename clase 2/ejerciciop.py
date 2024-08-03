dato1=int(input("Ingrese un numero: "))
dato2=int(input("Ingrese un numero: "))

if (dato1%2==0) and (dato2%2==1):
    print ("El dato 1 es par")
    print ("El dato 2 es impar")
elif (dato1%2==1) and (dato2%2==0):
    print ("El dato 2 es par")
    print ("El dato 1 es impar")
elif (dato1%2==0) and (dato2%2==0):
    print ("Ambos son positivos")