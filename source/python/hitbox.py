

class Hitbox:

    def __init__(self, x=81, y=81,  ancho=63, alto=80, visible=False, color=0, grosor=1):
        """
        Parameters
        ----------
        x : int o float, default 81
            Coordenada x del hitbox.

        y : int o float, default 81
            Coordenada y del hitbox.

        ancho : int o float, default 63
            Ancho del hitbox.

        alto : int o float, default 80
            Alto del hitbox.

        visible : bool, default False
            Determina si el hitbox se muestra al llamar el metodo display.

        color : int, default 0
            Color del contorno del hitbox.

        grosor : int, default 1
            Grosor del contorno del hitbox
        """
        self.visible = visible
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color
        self.grosor = grosor

    def display(self):
        """
        Muestra el hitbox si el parametro visible = True
        en caso contrario no muestra nada
        """
        if self.visible:
            noFill()
            rectMode(CENTER)
            stroke(self.color)
            strokeWeight(self.grosor)
            rect(self.x, self.y, self.ancho, self.alto)
    
    def setVisible(self, visible):
        self.visible = visible

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
        """
        Returns
        -------
        int o float
            Retorna la coordenada "Y" de la parte superior del hitbox.
        """
        return self.y - (self.alto / 2)

    def izquierda(self):
        """
        Returns
        -------
        int o float
            Retorna la coordenada "X" de la parte izquierda del hitbox.
        """
        return self.x - (self.ancho / 2)

    def abajo(self):
        """
        Returns
        -------
        int o float
            Retorna la coordenada "Y" de la parte inferior del hitbox.
        """
        return self.y + (self.alto / 2)

    def derecha(self):
        """
        Returns
        -------
        int o float
            Retorna la coordenada "X" de la parte derecha del hitbox.
        """
        return self.x + (self.ancho / 2)

    def aribaDerecha(self):
        """
        Returns
        -------
        tuple
            Retorna la coordenada (X, Y) de la esquina superior derecha del hitbox.
        """
        return (self.derecha(), self.arriba())

    def aribaIzquierda(self):
        """
        Returns
        -------
        tuple
            Retorna la coordenada (X, Y) de la esquina superior izquierda del hitbox.
        """
        return (self.izquierda(), self.arriba())

    def abajoDerecha(self):
        """
        Returns
        -------
        tuple
            Retorna la coordenada (X, Y) de la esquina inferior derecha del hitbox.
        """
        return (self.derecha(), self.abajo())

    def abajoIzquierda(self):
        """
        Returns
        -------
        tuple
            Retorna la coordenada (X, Y) de la esquina inferior izquierda del hitbox.
        """
        return (self.izquierda(), self.abajo())

    def contiene(self, x, y):
        """
        Determina si las coordenadas dadas estan dentro del hitbox

        Parameters
        ----------
        x : int o float
            Coordenada x del punto.

        y : int o float
            Coordenada y del punto.

        Returns
        -------
        Bool
            Retorna True si las coordenadas dadas estan dentro del hitbox, retorna False en caso contrario.
        """
        if(self.izquierda() < x and x < self.derecha()):
            return self.arriba() < y and self.abajo() > y
        return False

    def intersecta(self, hitbox):
        """
        Determina si el hitbox intersecta con otro hitbox dado

        Parameters
        ----------
        hitbox : Hitbox
            Hitbox a comparar.

        Returns
        -------
        Bool
            Retorna True si la hitbox dada intersecta con el hitbox propio, retorna False en caso contrario.
        """
        if self.izquierda() < hitbox.derecha() and self.derecha() > hitbox.izquierda():
            return self.arriba() < hitbox.abajo() and self.abajo() > hitbox.arriba()
        return False
