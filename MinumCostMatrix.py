import random
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