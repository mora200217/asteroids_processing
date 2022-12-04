

class Jugador:
    def __init__(self, x, y, hitbox, lista_keys, velocidad=2, velocidadGiro=1):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidad = velocidad
        self.velocidadGiro = velocidadGiro
        self.lista_keys = lista_keys
        self.hitbox = hitbox

    def setPosicion(self, x, y):
        self.x = x
        self.y = y
        self.hitbox.setPosicion(x, y)

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
        if len(self.lista_keys) == 0:
            return

        if "a" in self.lista_keys:
            self.girarDerecha()
        elif "d" in self.lista_keys:
            self.girarIzquierda()

        if "w" in self.lista_keys:
            catetoOpuesto = sin(radians(self.angulo))
            catetoAdyacente = sqrt(1 - pow(catetoOpuesto, 2))

            if self.angulo > 90 and self.angulo < 270:
                catetoAdyacente = catetoAdyacente * -1

            x = self.x + (catetoAdyacente * self.velocidad)
            y = self.y + (catetoOpuesto * self.velocidad)

            if x > width + 20:
                x = -20
            if x < -20:
                x = width + 20
            if y > height + 20:
                y = -20
            if y < -20:
                y = height + 20
            
            self.setPosicion(x,y)

    def display(self):
        self.hitbox.display()
        print(self.hitbox.arriba())
        stroke(204, 102, 0)
        translate(self.x, self.y)
        rotate(radians(self.angulo + 90))
        triangle(- 10, 20, 0, - 20,   10,  20)
