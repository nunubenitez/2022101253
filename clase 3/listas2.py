#en in solo va a devolver con true, con index la posicion y count cuenta cuantas veces hay
#sort es ordenar
array1=["futbol", "Pc", 18.6, 18, [6,7,10.4], True, False, "Pc"]
array2=[200, 250, "hola"]
array3=array1+array2
print(array3)

print("Pc" in array1)
print(array1.index("Pc"))

print(array1.count("Pc"))
array1.remove("Pc")
print(array1)
array1.reverse()
print(array1)
array4=[1,2,8,-11,5]
array4.sort()
print(array4)