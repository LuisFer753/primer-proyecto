def agrega_tarea():
  with open('num_de_tareas.txt', 'r') as num:
    actual=num.read()
  with open('num_de_tareas.txt', 'w') as num:
    num.write(str(int(actual)+1))
  with open('num_de_tareas.txt', 'r') as num:
    return(num.read())

def elimina_tarea():
  with open('num_de_tareas.txt', 'r') as num:
    actual=num.read()
  with open('num_de_tareas.txt', 'w') as num:
    num.write(str(int(actual)-1))
  with open('num_de_tareas.txt', 'r') as num:
    return(num.read())


accion=input('Qué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\n')

if accion=='a':
  print(agrega_tarea())

elif accion=='e':
  print(elimina_tarea())

else:
  print('no existe otra acción... de momento.')

