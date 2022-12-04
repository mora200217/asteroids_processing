

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

    def girarIzquierda(self):
        self.setAngulo(self.getAngulo() + (10 * self.velocidadGiro))

    def girarDerecha(self):
        self.setAngulo(self.getAngulo() - (10 * self.velocidadGiro))


    def update(self):
        if not keyPressed:
            return
            
        if key == "a":
            self.girarDerecha()
        elif key == "d":
            self.girarIzquierda()

        if key == "w":
            catetoOpuesto = sin(radians(self.angulo))
            catetoAdyacente = sqrt(1 - pow(catetoOpuesto, 2))

            if self.angulo > 90 and self.angulo < 270:
                catetoAdyacente = catetoAdyacente * -1

            self.x = self.x + (catetoAdyacente * self.velocidad)
            self.y = self.y + (catetoOpuesto * self.velocidad)

            if self.x > width + 20:
                self.x = -20
            if self.x < -20:
                self.x = width + 20
            if self.y > height + 20:
                self.y = -20
            if self.y < -20:
                self.y = height + 20

    def display(self):
        stroke(204, 102, 0)
        translate(self.x, self.y)
        rotate(radians(self.angulo + 90))
        triangle(- 10, 20, 0, - 20,   10,  20)
