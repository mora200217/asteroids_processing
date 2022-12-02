class Hitbox:
    def __init__(self, x=81, y=81,  ancho=63, alto=80, visible=False, color = 0, grosor = 3):
        self.visible = visible
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.grosor = grosor
    
    def display(self):
        if self.visible:
            noFill()
            rectMode(CENTER)
            stroke(self.color)
            stroke_weight(self.grosor)
            rect(self.x, self.y, self.ancho, self.alto)
    
    def setPosicion(self, x, y):
        self.x = x
        self.y = y

    def setTamano(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def getAlto(self):
        return self.alto

    def getAncho(self):
        return self.ancho

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def arriba(self):
        return self.y - (self.alto / 2)

    def izquierda(self):
        return self.x - (self.ancho / 2)

    def abajo(self):
        return self.y + (self.alto / 2)

    def derecha(self):
        return self.x + (self.ancho / 2)
    
    def aribaDerecha(self):
        return (self.derecha(), self.arriba())

    def aribaIzquierda(self):
        return (self.izquierda(), self.arriba())

    def abajoDerecha(self):
        return (self.derecha(), self.abajo())

    def abajoIzquierda(self):
        return (self.izquierda(), self.abajo())
    
    def contiene(self, x, y):
        if(self.izquierda() < x and x < self.derecha()):
            return self.arriba() < y and self.abajo() > y
        return False

    def intersecta(self, hitbox):
        if self.izquierda() < hitbox.derecha() and self.derecha() > hitbox.izquierda():
            return self.arriba() < hitbox.abajo() and self.abajo() > hitbox.arriba()
        return False
