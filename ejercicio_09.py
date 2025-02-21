# Para implementar un reloj digital es necesario declarar tres variables, para controlar: horas, minutos y segundos. Cada una de estas variables controla un ciclo, así: los segundos se incrementan desde 0 a 59, los minutos también desde 0 a 59 y las horas desde 1 a 12 o de 1 a 24. Este algoritmo está diseñado para terminar la ejecución al llegar a 12:59:59

#declaramos variables 
horas = 1
minutos = 0
segudnos = 0

while horas <= 12:
    while minutos <=59:
        while segudnos <=59:
            print(f"{horas:02d}:{minutos:02d}:{segudnos:02d}")
            segudnos += 1
        minutos += 1
        segudnos += 0
    horas += 1
    minutos = 0
            
            
            