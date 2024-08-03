'''
crea un programa que permisa al usuario ingresar una lista de numeros.
'''
def ingresar_num():
            numeros = []
            while True:
                num = input("Ingrese un numero o 'n' para terminar")
                if num.lower == 'n':
                    break
                numeros.append(float(num))
                return numeros
            
def suma_num(numeros):
     suma=0
     for numero in numeros:
        suma += numero
     return suma

def calcular_promedio(numeros):
     suma = suma_num (numeros)
     promedio = suma / len(numeros)
     return promedio

def encontrar_max_min(numeros):
     maximo = max(numeros)
     minimo = min(numeros)
     return maximo, minimo
def num_mayor_prom(numeros, promedio):
  promedio.index(numeros)
  return numeros    
def main():
    num = ingresar_num()
    if len(num) == 0:
        print ("No se ingreso ningun numero.")
        return
    suma = suma_num (num)
    promedio = calcular_promedio(num)
    maximo, minimo = encontrar_max_min(num)
    mayores = num_mayor_prom(num, promedio)
    print(f"Numeros ingresados: {num}")
    print(f"Suma de los numeros: {suma}")
    print(f"Numero mas grande: {maximo}")
    print(f"Numero mas pequenho: {minimo} ")
    print(f"Numeros mayores que el promedio: {mayores}")

    if __name__ == "__main__":
        main()