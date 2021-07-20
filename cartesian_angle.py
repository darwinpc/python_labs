class CartesianAngle:
    def __init__(self, angle):
        self.angle = angle
    def calculate(self):
        if self.angle.isdigit():
            module = int(self.angle) % 360
            print("Residuo: {}".format(module))

            if self.angle == 0 or module == 0:
              print ("Es el origen")
            if (self.angle > 0 and self.angle <= 90) or (module > 0 and module <= 90):
              print("Cuadrante I")
            if (self.angle > 90 and self.angle <= 180) or (module > 90 and module <= 180):
              print("Cuadrante II")
            if (self.angle > 180 and self.angle <= 270) or (module > 180 and module <= 270):
              print ("Cuadrante III")
            if (self.angle > 270 and self.angle <= 360) or (module > 270 and module <= 360):
              print ("Cuadrante IV")
        else:
            print("Ingresa un dato valido.")

angle = str(input("Proporcionar angulo: "))
cartesian_angle = CartesianAngle(angle)
cartesian_angle.calculate()
