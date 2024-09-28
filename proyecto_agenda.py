def agrega_numerode_tarea():
    with open('num_de_tareas.txt', 'r') as num:
        actual=num.read()
    with open('num_de_tareas.txt', 'w') as num:
        num.write(str(int(actual)+1))
    with open('num_de_tareas.txt', 'r') as num:
        return(num.read())

def elimina_numerode_tarea():
    with open('num_de_tareas.txt', 'r') as num:
        actual=num.read()
    with open('num_de_tareas.txt', 'w') as num:
        num.write(str(int(actual)-1))
    with open('num_de_tareas.txt', 'r') as num:
        return(num.read())


tareas=[]
accion=input('Qué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\nterminar programa (t)\n')

while True:
    if accion=='a':
        tarea=input('Escribe la tarea que quieres agregar: ')
        tareas.append(tarea)
        print(agrega_numerode_tarea())
        print(f'"{tarea}" ha sido agregada en tu agenda')

    elif accion=='e':
        print(elimina_numerode_tarea())
        
    elif accion=='t':
        print('programa terminado')
        break

    else:
        print('no existe otra acción... de momento.')
        accion=input('Qué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\nterminar programa (t)\n')


