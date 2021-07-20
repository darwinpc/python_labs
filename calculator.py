def switch(case, a, b):
  sw = {1:suma(a, b), 2: resta(a, b), 3: multiplicacion(a, b), 4: division(a, b)}
  return sw.get(case)

def suma(a, b):
    return "La suma de {} y {} es: {}".format(a, b, a + b)
def resta(a, b):
    return "La resta de {} y {} es: {}".format(a, b, a - b)
def multiplicacion(a, b):
    return "La multiplicacion de {} y {} es: {}".format(a, b, a * b)
def division(a, b):
    return "La division de {} y {} es: {}".format(a, b, a / b)

def menu():
  print("----------- Calculadora -----------")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicacion")
  print("4. Division")
  print("-----------------------------------")

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
menu()
case = int(input("Seleccione una opcion: "))
print(switch(case, a, b))
