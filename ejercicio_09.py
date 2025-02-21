# Para implementar un reloj digital es necesario declarar tres variables, para controlar: horas, minutos y segundos. Cada una de estas variables controla un ciclo, así: los segundos se incrementan desde 0 a 59, los minutos también desde 0 a 59 y las horas desde 1 a 12 o de 1 a 24. Este algoritmo está diseñado para terminar la ejecución al llegar a 12:59:59

#importar time

import time

#declaramos variables 
horas = 1
minutos = 0
segundos = 0

while horas <= 12:
    while minutos <=59:
        while segundos <=59:
            print(f"{horas}:{minutos}:{segundos}")
            segundos += 1
        minutos += 1
        segundos += 0 #reiniciar segundo al cambiar de minutos
    horas += 1
    minutos = 0 #reiniciar minutos al cambiar de hora
            
            
            