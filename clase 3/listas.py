'''
lista en python
'''

array=["futbol", "PC", 18.6, 18, [6,7,10,4], True, False]
print (array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])
print(len(array))

array.append(66) #'es para anhadir algo a la lista'. para tomar referencia esto es vectores 
print(array)
array.insert(1,88) #insertar datos en una posicion
print(array)
array.extend([1, 88, True, 100]) #insertar  mas de un dato en una misma posicion (?)
print(array)