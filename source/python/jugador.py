

class Jugador:
    def __init__(self, x, y, hitbox, lista_keys, velocidadMaxima=2, aceleracion=0.1, friccion=0.1, velocidadGiro=1):
        self.x = x
        self.y = y

        # Ajustando parametros velocidad inicial
        self.velocidad = 0
        self.velocidadMaxima = velocidadMaxima
        self.aceleracion = aceleracion
        self.friccion = friccion
        self.dx = 0
        self.dy = 0

        self.angulo = 0
        self.velocidadGiro = velocidadGiro

        self.hitbox = hitbox
        self.hitbox.setPosicion(x, y)

        self.lista_keys = lista_keys
        self.teclas = {"izquierda": "a",
                       "derecha": "d",
                       "avanzar": "w"
                       }

    def setPosicion(self, x, y):
        if x > width + 20:
            x = -20
        if x < -20:
            x = width + 20
        if y > height + 20:
            y = -20
        if y < -20:
            y = height + 20
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
        self.setAngulo(self.getAngulo() - (10 * self.velocidadGiro))

    def girarDerecha(self):
        self.setAngulo(self.getAngulo() + (10 * self.velocidadGiro))

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion
        if self.velocidad >= self.velocidadMaxima:
            self.velocidad = self.velocidadMaxima

    def frenar(self):
        self.velocidad = self.velocidad - self.friccion
        if self.velocidad < 0:
            self.velocidad = 0

    def getCatetos(self):
        catetoOpuesto = sin(radians(self.angulo))
        catetoAdyacente = sqrt(1 - pow(catetoOpuesto, 2))

        if self.angulo > 90 and self.angulo < 270:
            catetoAdyacente = catetoAdyacente * -1

        return catetoOpuesto, catetoAdyacente
    
    def calcularPocicion(self):
        catetoOpuesto,catetoAdyacente = self.getCatetos()

        self.dx = catetoAdyacente * self.velocidad
        self.dy = catetoOpuesto * self.velocidad
        x = self.x + self.dx
        y = self.y + self.dy

        self.setPosicion(x, y)
        
    def update(self):
        if not keyPressed:
            self.frenar()
            self.calcularPocicion()
            return

        if self.teclas["izquierda"] in self.lista_keys:
            self.girarIzquierda()

        elif self.teclas["derecha"] in self.lista_keys:
            self.girarDerecha()

        if self.teclas["avanzar"] in self.lista_keys:
            self.acelerar()
            self.calcularPocicion()

        else:
            self.frenar()
            self.calcularPocicion()

    def display(self):
        self.hitbox.display()
        stroke(204, 102, 0)
        translate(self.x, self.y)
        rotate(radians(self.angulo + 90))
        triangle(- 10, 20, 0, - 20,   10,  20)
