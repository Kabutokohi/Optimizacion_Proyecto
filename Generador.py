import numpy as np
import random as rd
import os
from shutil import rmtree as rm

proyectos = [(10,30),(10,30),(10,30),
             (40,60),(40,60),(40,60),
             (70,90),(70,90),(70,90),
             (100,300),(100,300),(100,300),
             (400,600),(400,600),(400,600),
             (700,900),(700,900),(700,900),
             (1000,3000),(1000,3000),(1000,3000),
             (4000,6000),(4000,6000),(4000,6000),
             (7000,9000),(7000,9000),(7000,9000)]
personas = [(10,30),(40,60),(70,90),
            (10,30),(40,60),(70,90),
            (10,30),(40,60),(70,90),
            (100,300),(400,600),(700,900),
            (100,300),(400,600),(700,900),
            (100,300),(400,600),(700,900),
            (1000,3000),(4000,6000),(7000,9000),
            (1000,3000),(4000,6000),(7000,9000),
            (1000,3000),(4000,6000),(7000,9000)]

"""
Presupuesto para cada proyecto    
"""
def project_budget(M=27):
    budget = list()
    rd.seed(10)
    for x in range(M):
        budget.append(rd.randint(11111,99999))
    return budget

"""
    Genera una lista de enteros aleatorios entre 11111 y 99999 que se entienden como el
    lo que cobra cada persona por hora al trabajar
    
    :param cantPeople: Numero de personas en el proyecto.
    :return: Una lista de enteros aleatorios entre  11111 y 99999.
"""
def CostPerPersonPerHour(cantPeople):
    rd.seed(15)
    costPerson = list()
    for i in range(cantPeople):
        costPerson.append(rd.randint(11111,99999))
    return costPerson
"""
Genera una lista con el maximo de horas mensuales por persona.
"""
def MaxMonthlyHour(cantPeople):
    rd.seed(15)
    MaxHour = list()
    for i in range(cantPeople):
        MaxHour.append(rd.randint(11111,99999))
    return MaxHour
"""
Genera una lista con el minimo de horas mensuales que debe tener cada proyecto
"""
def MinMonthlyHour(cantProyect):
    rd.seed(10)
    MinHour = list()
    for i in range(cantProyect):
        MinHour.append(rd.randint(11111,99999))
    return MinHour

'''
    Genera la cantidad de proyectos y la cantidad de personas 
    disponibles a ese proyecto el retorno tiene el siguiente orden
    cantidad de proyectos, cantidad de personas.
'''
def numberOfProyectAndPeople(Proyect=proyectos,People=personas,iteraciones=27):
    rd.seed(10)
    proyectAndPeople = list()
    arch = open("cantidad_Poyect_and People.txt","w")
    for x in range(iteraciones-1):
        arch.write("Proyecto {0}\n".format(x+1))
        cantProyect = rd.randint(Proyect[x][0], Proyect[x][1]) 
        cantPeople = rd.randint(People[x][0],People[x][1])
        arch.write("cantidad de proyectos: {0}\n".format(cantProyect))
        arch.write("cantidad de personas: {0}\n".format(cantPeople))
        arch.write("\n")
        proyectAndPeople.append([cantProyect,cantPeople])
    arch.close()
    proyectAndPeople.append([10,10])
    return proyectAndPeople

def CreationOfIntances():
    os.makedirs('Intancias_de_prueba/',exist_ok =True)
    cantProAndPe = numberOfProyectAndPeople()
    Intancia = 1
    for proyect, people in cantProAndPe:
        arch = open("Intancias_de_prueba/Intancia_{0}.txt".format(Intancia),"w")
        if proyect > people:
            arch.write("hago algo")
            #print("hago algo")
        elif proyect == people:
            cost_person = CostPerPersonPerHour(people)
            arch.write("/* Objective function */\n")
            arch.write("min: ")
            for i in range(people):
                for j in range(proyect):
                    costoxmatriz = "{0} x{1}{2}".format(cost_person[j],i,j)
                    if j < proyect - 2:
                        arch.write(costoxmatriz+" + ")
                    else:
                        arch.write(costoxmatriz+";\n")
            arch.write("/* Contrains */\n")
            for i in range(people):
                for j in range(proyect):
                    arch.write("bin x{}{};\n".format(i,j))
            #print("hago una cosa distinta")
        else:
            arch.write("hago algo")
            #print("hago otra cosa")
        Intancia+=1
        arch.close()

CreationOfIntances()
    
    
            
            
        
    
    





        
    




        
    
    