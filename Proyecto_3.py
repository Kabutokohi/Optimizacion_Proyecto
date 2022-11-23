import random

#Método del Mínimo costo
def Matriz_de_Minimo_costo(oferta,demanda,costos,asignado):
    while sum(oferta) > 0:
        Menor = []
        for i in range(len(oferta)):
            if oferta[i] > 0:
                for j in range(len(demanda)):
                    if demanda[j] > 0:
                        if len(Menor) == 0:
                            Menor.append([costos[i][j],i,j])
                        else:
                            if costos[i][j] < Menor[0][0]:
                                Menor = [[costos[i][j],i,j]]
                            elif costos[i][j] == Menor[0][0]:
                                Menor.append([costos[i][j],i,j])
        _,x,y = random.choice(Menor)
        if oferta[x] >= demanda[y]:
            oferta[x] -= demanda[y]
            asignado[x][y] = demanda[y]
            demanda[y] = 0
        else:
            demanda[y] -= oferta[x]
            asignado[x][y] = oferta[x]
            oferta[x] = 0
    return asignado

#Aproximación de Russell
def Aproximacion_de_Russell(oferta,demanda,costos,asignado,ICs):
    while sum(oferta) > 0:
        #Mayor por columna
        for i in range(len(oferta)):
            Mayor = 0
            if oferta[i] > 0:
                for j in range(len(demanda)):
                    if demanda[j] > 0:
                        if Mayor < costos[i][j]:
                            Mayor = costos[i][j]
            #Tenemos el mayor de la columna por lo que se suma y se quita el costo
            for j in range(len(demanda)):
                if demanda[j] > 0:
                    ICs[i][j] = Mayor - costos[i][j]
                else:
                    ICs[i][j] = 0
        #Mayor por fila
        for j in range(len(demanda)):
            Mayor = 0
            if demanda[j] > 0:
                for i in range(len(oferta)):
                    if oferta[i] > 0:
                        if Mayor < costos[i][j]:
                            Mayor = costos[i][j]
                    
            #Tenemos el mayor de la fila por lo que suma
            for i in range(len(oferta)):
                if oferta[i] > 0:
                    ICs[i][j] += Mayor
                else:
                    ICs[i][j] = 0
        Mayor_IC = []
        for i in range(len(oferta)):
            if oferta[i] > 0:
                for j in range(len(demanda)):
                    if demanda[j] > 0:
                        if len(Mayor_IC) == 0:
                            Mayor_IC.append([ICs[i][j],i,j])
                        else:
                            if ICs[i][j] > Mayor_IC[0][0]:
                                Mayor_IC = [[ICs[i][j],i,j]]
                            elif ICs[i][j] == Mayor_IC[0][0]:
                                Mayor_IC.append([ICs[i][j],i,j])
        _,x,y = random.choice(Mayor_IC)
        if oferta[x] >= demanda[y]:
            oferta[x] -= demanda[y]
            asignado[x][y] = demanda[y]
            demanda[y] = 0
        else:
            demanda[y] -= oferta[x]
            asignado[x][y] = oferta[x]
            oferta[x] = 0
    return asignado


o = int(input("Ingrese la cantidad de nodos de oferta: "))
d = int(input("Ingrese la cantidad de nodos de demanda: "))

total = 0
while total <= 0:
    total  = int(input("Ingrese la cantidad total de oferta/demanda: "))

costo = 0
while costo <= 0:
    costo = int(input("Ingrese el valor del costo máximo en la matriz: "))

# Creación de la oferta
oferta_total = total
oferta = []
oferta_2 = []
for i in range(o):
    if i < o-1:
        rand = random.randint(0,oferta_total)
        oferta_total -= rand
        oferta.append(rand)
        oferta_2.append(rand)
    else:
        if oferta_total > 0:
            oferta.append(oferta_total)
            oferta_2.append(oferta_total)
        else:
            oferta.append(0)
            oferta_2.append(0)

# Creación de la demanda
demanda_total = total
demanda = []
demanda_2 = []
for i in range(d):
    if i < d-1:
        rand = random.randint(0,demanda_total)
        demanda_total -= rand
        demanda.append(rand)
        demanda_2.append(rand)
    else:
        if demanda_total > 0:
            demanda.append(demanda_total)
            demanda_2.append(demanda_total)
        else:
            demanda.append(0)
            demanda_2.append(0)

#Inicialización de matriz de costos y matriz con los valores asignados (inicialmente 0)
costos = []
asignado = []
asignado_2 = []
ICs = []
for i in range(o):
    costos.append([])
    asignado.append([])
    asignado_2.append([])
    ICs.append([])
    for j in range(d):
        costos[i].append(random.randint(1,costo))
        asignado[i].append(0)
        asignado_2[i].append(0)
        ICs[i].append(0)


print("\nOferta")
print(oferta)
print("Demanda")
print(demanda)
print("Matriz de Costos")
print(costos)

#Para el algoritmo de Mínimo costo
asignado = Matriz_de_Minimo_costo(oferta,demanda,costos,asignado)
print("\nResultado por método de matriz de Mínimo costo")
z = 0
arreglo = "Z = "
for i in range(len(oferta)):
    for j in range(len(demanda)):
        if asignado[i][j] > 0:
            z += asignado[i][j]*costos[i][j]
            arreglo += str( asignado[i][j]) + "*" + str(costos[i][j]) + " + "
arreglo = arreglo.strip(" + ")
print("Z = " + str(z))
print(arreglo)

#Para el algoritmo de Russell
asignado_2 = Aproximacion_de_Russell(oferta_2,demanda_2,costos,asignado_2,ICs)

print("\nResultado por método de Russell")
z = 0
arreglo = "Z = "
for i in range(len(oferta)):
    for j in range(len(demanda)):
        if asignado_2[i][j] > 0:
            z += asignado_2[i][j]*costos[i][j]
            arreglo += str( asignado_2[i][j]) + "*" + str(costos[i][j]) + " + "
arreglo = arreglo.strip(" + ")
print("Z = " + str(z))
print(arreglo)