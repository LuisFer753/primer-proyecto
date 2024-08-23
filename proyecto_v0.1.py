accion=input('Qué quieres hacer?\nagregar tarea (a)\neliminar tarea (e)\n')

if accion=='a':
  with open('num_de_tareas.txt', 'r') as num:
    actual=num.read()
  with open('num_de_tareas.txt', 'w') as num:
    num.write(str(int(actual)+1)) #aqui una operación
  with open('num_de_tareas.txt', 'r') as num:
    print(num.read())

elif accion=='e':
  with open('num_de_tareas.txt', 'r') as num:
    actual=num.read()
  with open('num_de_tareas.txt', 'w') as num:
    num.write(str(int(actual)-1))  #aqui otra operacion
  with open('num_de_tareas.txt', 'r') as num:
    print(num.read())

else:
  print('no existe otra acción... de momento.')


















'''
def dolares_a_pesos(dolares):
  return float(dolares*19.41)

def costo_hotel(noches):
  return float(noches*185)

def costo_avion(pasajeros):
  return float(pasajeros*410)

def costo_viaje(noches,pasajeros):
  return float(dolares_a_pesos(costo_hotel(noches)+costo_avion(pasajeros)))

# pide opción y dependiendo de la opción llama una función diferente
opcion = int(input())     
if(opcion == 1):
     dolares  = float(input())
     print(dolares_a_pesos(dolares))
elif(opcion == 2):
     noches  = int(input())
     print(costo_hotel(noches))
elif(opcion == 3):
     pasajeros  = int(input())
     print(costo_avion(pasajeros))
elif(opcion == 4):
    noches  = int(input())
    pasajeros  = int(input())
    print(costo_viaje(noches,pasajeros))
'''