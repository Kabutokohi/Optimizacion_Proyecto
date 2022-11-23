<h1> Descripción: </h1>

Existen N personas que deben ser asignadas a M proyectos conociendo los siguientes datos:
-  Presupuesto para cada proyecto. (listo) **project_budget(M=27)**

- Costo por hora de asignar una persona a un proyecto. (listo) **CostPerPersonPerHour(cantPeople)**

- Máximo de horas mensuales que una persona puede trabajar. (listo) **MaxMonthlyHour(cantPeople)**

- Mínimo de horas mensuales que deben ser completadas en cada proyecto. **MinMonthlyHour(cantProyect)**

La asignación debe cumplir que: **restricciones**

- El número de personas asignadas a un proyecto puede ser a lo más cinco.

- El número de proyectos asignados a una persona puede ser a lo más cinco.

- El costo de asignación en cada proyecto no puede superar su correspondiente presupuesto.

<h1>Dado el problema presentado anteriormente: </h1>

1. Defina el modelo matemático correspondiente si se desea Minimizar:
    
    a) Costo total de la asignación.

    b) Cantidad total de horas trabajadas.

2. Genere al menos 27 instancias de prueba factibles del problema, 1 de cada dimensión descrita en la tabla. 

3. Exponga detenidamente el proceso de generación de instancias. 

    - Qué condiciones deben cumplir los parámetros, ya sea independientemente o conjuntamente, para lograr la factibilidad de la instancia de prueba.

    - Cómo maneja la aleatoriedad.

4. Resuelva las instancias de prueba propuestas utilizando:

    a) LPSolve

    b) Minizinc

5. Resuelva las instancias de prueba propuestas mediante la implementación de:

    a) Métodos del mínimo costo en la matriz y de aproximación de Vogel (VAM).

    b) Métodos de la esquina nor-oeste y de Houthakken.

6. Presente los resultados obtenidos para cada una de las instancias de prueba propuestas en cada enfoque solicitado entregando:

    - Tiempo de ejecución y/o cantidad de iteraciones.

   - Calidad de la solución.

   - Cantidad de variables.

   - Otros.

7. Analice y compare los resultados obtenidos para cada una de las instancias de prueba propuestas en cada enfoque solicitado, con respecto a:

    - Tiempo de ejecución y/o cantidad de iteraciones.

    - Calidad de la solución.

    - Cantidad de variables.

    - Otros.


En los puntos 1, 4 y 5 solo debe trabajar con los casos (a o b) que le sean asignados al equipo. (Ver descripción del equipo)
