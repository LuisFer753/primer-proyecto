def agrega_tarea(materia, tarea):
    fila=0
    for i in range(len(materias)):
        if materias[i]==materia:
            fila=i
    tareas[fila].append(tarea)
    print(tareas)
    return f'¡"{tarea}" ha sido agregada en tu agenda!'

def elimina_tarea(posicion):
    contador=1
    fila=0
    columna=0
    for i in tareas:
        for o in i:
            if contador==posicion:
                tarea=tareas[fila][columna]
                tareas[fila].remove(tarea)
                print(tareas)
                return f'¡"{tarea}" fue eliminada de tu agenda!'
            else:
                contador+=1
                columna+=1
        fila+=1
        columna=0

def muestra_tareas(nmateria):
    materia='?'
    fila=nmateria-1
    materia=materias[fila]
    print(f'Tareas de {materia}:\n')
    for o in tareas[fila]:
        print(o)

tareas=[]
materias=[]
nmaterias=int(input('Cuántas materias tienes? '))
for i in range(nmaterias):
    tareas.append([])
aux='una'
for o in range(nmaterias):
    materia=input(f'escribe el nombre de {aux} materia que tengas: ')
    materias.append(materia)
    aux='otra'
accion=input('\n\nQué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\nmostrar tareas (m)\nterminar programa (t)\n')

while True:
    if accion=='a':
        materia=input('¿De qué materia es la tarea que quieres agregar? ')
        esta='no'
        while esta=='no':
            if materia in materias:
                esta='si'
            else:
                materia=input('Esa materia no se encuentra entre tus materias registradas, escribe una materia que esté registrada o escrcibe la materia correctamente: ')
        tarea=input('Escribe la tarea que quieres agregar: ')
        print(agrega_tarea(materia, tarea))


    elif accion=='e':
        num=1
        for i in tareas:
            for o in i:
                print(f'{num}- {o}')
                num+=1
        elimina=int(input('Elije el número de la tarea que quieres eliminar: '))
        esta='no'
        while esta=='no':
            if elimina<1 or elimina>num-1:
                elimina=int(input('El número de la tarea no es válido, intenta de nuevo: '))
            else:
                esta='si'
        print(elimina_tarea(elimina))


    elif accion=='m':
        modo=int(input('¿Quieres ver todas tus tareas o solo las de una materia especifica? (1/2) '))
        esta='no'
        while esta=='no':
            if modo==1 or modo==2:
                esta='si'
            else:
                modo=int(input('respuesta inválida, escribe "1" si quieres ver todas tus tareas o "2" si solo quieres ver las de una materia específica: '))
        if modo==1:
            for i in tareas:
                for o in i:
                    print(o)

        else:
            num=1
            for i in materias:
                print(f'{num}- {i}')
                num+=1
            mat=int(input('Elije el número de la materia cuyas tareas quieres ver: '))
            esta='no'
            while esta=='no':
                if mat<1 or mat>num-1:
                    mat=int(input('El número de materia no es válido, intenta ded nuevo: '))
                else:
                    esta='si'
            muestra_tareas(mat)

        
    elif accion=='t':
        print('programa terminado')
        break

    else:
        print('no existe otra acción. Elije una opción válida')
        accion=input('Qué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\nterminar programa (t)\n')

    accion=input('\n\nQué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\nmostrar tareas (m)\nterminar programa (t)\n')


