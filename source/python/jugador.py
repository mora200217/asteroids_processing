

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidad = 2
        self.velocidadGiro = 2


    def setPosicion(self, x, y):
        self.x = x
        self.y = y

    def setAngulo(self, angulo):

        self.angulo = angulo
        if self.angulo > 360:
            self.angulo = 0
        elif self.angulo < 0:
            self.angulo = 360

    def getAngulo(self):
        return self.angulo
