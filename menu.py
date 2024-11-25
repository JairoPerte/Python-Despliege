import operaciones

# Función para mostrar el menú
def mostrar_menu():
   opcion=0
   while(opcion<1 or opcion>5):
      print("1- sumar, 2- restar, 3- multiplicar, 4-dividir y 5- salir")
      opcion = int(input("¿Qué opción elige? "))
   opciones(opcion)

# Función para mostrar la opcción
def opciones(opcion):
   if(opcion!=5):
      num1 = input("¿Cuál es el primer número 1? ")
      num2 = input("¿Cuál es el primer número 2? ")
   match opcion:
      case 1:
         solucion=operaciones.sumar(num1,num2)
      case 2:
         solucion=operaciones.restar(num1,num2)
      case 3:
         solucion=operaciones.multiplicar(num1,num2)
      case 4:
         if(num2 != "0"):
            solucion=operaciones.dividir(num1,num2)

   if(opcion != 5):
      try:
         if(solucion != False):
            print(f"La solución es {solucion}")
         else:
            print("Alguno de los números no son enteros o floats")
      except NameError:
            print("El divisor no puede ser 0")
      mostrar_menu()
