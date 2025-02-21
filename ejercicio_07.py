# Una joyería establece el valor de sus productos según el peso y el material. Se requiere un algoritmo que lea un valor de referencia x y a partir de éste calcule el valor del gramo de material utilizado y el valor del producto. El gramo de plata procesado tiene un costo de 3x, el platino 5x y el oro 8x.

#leer el valor de referencia x

x = float (input("Ingresar el valor de referencia x: "))

#leer el material utilizado

material = input("Ingresar el material utilizado (plata, platino, oro): ")

#calcular el valor del gramo de material utilizado

if material.lower () == "plata":
    valor_gramo = 3 * x

elif material.lower () == "platino":
    valor_gramo = 5 * x
    
elif material.lower () == "oro":
    valor_gramo = 8 * x
    
else: 
    print (" material no valido ")
    
# calcular el valor del producto

if valor_gramo > 0:
    peso = float(input("ingrese el peso del producto en gramos:"))
    valor_producto = valor_gramo * peso
    print (f"el valor del gramo de {material} es ${valor_gramo}")
    print (f"el valor del producto es: {valor_producto}")
else:
    print("no se puede calcular el valor del producto")