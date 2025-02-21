# Una joyería establece el valor de sus productos según el peso y el material. Se requiere un algoritmo que lea un valor de referencia x y a partir de éste calcule el valor del gramo de material utilizado y el valor del producto. El gramo de plata procesado tiene un costo de 3x, el platino 5x y el oro 8x.

#leer el valor de referencia x

x = float (input("Ingresar el valor de referencia x"))

#leer el material utilizado

material = input("Ingresar el material utilizado (plata, platino, oro): ")

#calcular el valor del gramo de material utilizado

if material () == "plata":
    valor_gramo = 3 * x

elif material () == "platino":
    valor_gramo = 5 * x
    
elif material () == "oro":
    valor_gramo = 8 * x
    
else: 
    print (" material no valido ")