#La distribuidora de motocicletas Rueda Floja ofrece una promoción que consiste en lo siguiente: las motos marca Honda tienen un descuento del 5%, las de marca Yamaha del 8%y las Suzuki el 10%, las de otras marcas el 2%. Se requiere calcular el valor a pagar por una motocicleta.

#pedir al usuario que ingrese la marca de la motocicleta
while True:
    #oedir al usuario que ingrese la marca de la motocicleta
    marca = input("Ingrese la marca de la motocicleta (honda, yamaha, suzuki u otra): ")
    #pedir al usuario que ingrese el precio de la motocicleta
    precio = float(input("ingre el precio de la motocicleta: $"))
    #calcular el descuento segun la marca
    if marca.lower () == "honda": 
        descuento = precio * 0.05
    elif marca.lower () == "yamaha":
        descuento = precio * 0.08
    elif marca.lower () == "suzuki":
        descuento = precio * 0.10
    else:
        marca () == "otra"
        descuento = precio * 0.02

#calcular el precio final 
    precio_final = precio - descuento
    #imprimir el resultado
    print(f"el precio final de la motocicleta es. $ {precio_final}")
    #preguntar al usuario si quiere seguir en el programa
    respuesta = input("quiere seguir calculando precios ? (s/n): ")
    if respuesta () != "s":
        #print("------el programa ha terminado !-----")

        break    
       