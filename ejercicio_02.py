#Se requiere un algoritmo que decida si un empleado tiene derecho al auxilio de transporte. Se conoce que todos los empleados que devengan un salario menor o igual a dos salarios mínimos legales tienen derecho a este rubro.

#definir salario minimo legal 
salario_minimo = 1200000


#pedir al usuario que ingrese el salario del empleado
salario_empleado = float(input("ingrese el salario del empleado: "))
#verificar si el empleado tiene derecho al auxilio de transporte
#if dara la condicion para saber si cumple con la condicion
if salario_empleado <= salario_minimo *2:
        print("El empleado tiene derecho al auxilio de transporte")
    
else:
        print ("Empleado gana mas de dos salarios \nEmpleado no tiene derecho a auxilio de transporte")
    


print("Programa finalizado.")