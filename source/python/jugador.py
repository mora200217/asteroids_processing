

class Jugador:
    def __init__(self, x, y, hitbox, lista_keys, velocidadMaxima=2, aceleracion=0.1, friccion=0.1, velocidadMaximaGiro=10, aceleracionGiro=0.1, friccionGiro=0.1):
        """
        Parameters
        ----------
        x : int o float
            Coordenada x inicial del Jugador.

        y : int o float
            Coordenada y inicial del Jugador.

        hitbox : Hitbox
            Hitbox para las colisiones.

        lista_keys : list of keys
            Lista que contiene las keys presionadas durante el programa.
        
        --------------------------------------------
        
        velocidadMaxima : int o float, default 2
            Velocidad maxima que alcanza el jugador.
        
        aceleracion : int o float, default 0.1
            Aceleracion que posee el jugador.
        
        friccion : int o float, default 0.1
            Friccion que se le aplica al jugador para frenarlo.
        
        --------------------------------------------
        
        velocidadMaximaGiro : int o float, default 0.1
            Velocidad maxima alcanzada al rotar sobre el propio eje, en grados.
        
        aceleracionGiro : int o float, default 0.1
            Aceleracion que se aplica al rotar sobre si mismo.
        
        friccionGiro : int o float, default 0.1
            Friccion que se le aplica al jugador para que deje de girar.      
        """
        self.x = x
        self.y = y

        # Ajustando parametros velocidad inicial
        self.velocidad = 0
        self.velocidadMaxima = velocidadMaxima
        self.aceleracion = aceleracion
        self.friccion = friccion
        self.dx = 0
        self.dy = 0

        # Ajustando parametros velocidad giro inicial
        self.angulo = 0
        self.velocidadGiro = 0
        self.velocidadMaximaGiro = velocidadMaximaGiro
        self.aceleracionGiro = aceleracionGiro
        self.friccionGiro = friccionGiro
        
        # Acomodando hitbox
        self.hitbox = hitbox
        self.hitbox.setPosicion(x, y)

        # Teclas presionadas
        self.lista_keys = lista_keys
        self.teclas = {"izquierda": "a",
                       "derecha": "d",
                       "avanzar": "w"
                       }

    def setPosicion(self, x, y):
        """
        Establece la posicion respetando el borde
        teletraspontandolo al llegar al borde
        """
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
        """
        Gira el jugador a la izquierda repetando la aceleracion y la velocidad maxima
        """
        self.velocidadGiro = self.velocidadGiro - self.aceleracionGiro
        
        if self.velocidadGiro > self.velocidadMaximaGiro:
            self.velocidadGiro = self.velocidadMaximaGiro

        self.setAngulo(self.getAngulo() + self.velocidadGiro)

    def girarDerecha(self):
        """
        Gira el jugador a la derecha repetando la aceleracion y la velocidad maxima
        """
        self.velocidadGiro = self.velocidadGiro + self.aceleracionGiro
        
        if self.velocidadGiro > self.velocidadMaximaGiro:
            self.velocidadGiro = self.velocidadMaximaGiro

        self.setAngulo(self.getAngulo() + self.velocidadGiro)

    def frenarGiro(self):
        """
        Disminuye la velocidad del giro respetando la friccion de giro
        """
        if self.velocidadGiro > 0:
            self.velocidadGiro = self.velocidadGiro - self.friccionGiro
            
            if self.velocidadGiro < 0:
                self.velocidadGiro = 0

        elif self.velocidadGiro < 0:
            self.velocidadGiro = self.velocidadGiro + self.friccionGiro
            
            if self.velocidadGiro > 0:
                self.velocidadGiro = 0

        self.setAngulo(self.getAngulo() + self.velocidadGiro)

    def acelerar(self):
        """
        Aplica la aceleracion al jugador respetendo la variable de aceleracion
        """
        self.velocidad = self.velocidad + self.aceleracion
        
        if self.velocidad >= self.velocidadMaxima:
            self.velocidad = self.velocidadMaxima

    def frenar(self):
        """
        Disminuye la velocidad al jugador respetando la friccion
        """
        self.velocidad = self.velocidad - self.friccion
        
        if self.velocidad < 0:
            self.velocidad = 0

    def getCatetos(self):
        """
        Retorna los catetos de un triangulo rectangulo de hipotenusa 1 y el angulo del jugador para facilitar calculos

        Returns
        -------
        catetoOpuesto float
            Retorna el cateto opuesto con respeco al angulo del jugador.

        catetoAdyacente float
            Retorna el cateto adyacente con respeco al angulo del jugador.
        """
        catetoOpuesto = sin(radians(self.angulo))
        catetoAdyacente = sqrt(1 - pow(catetoOpuesto, 2))

        if self.angulo > 90 and self.angulo < 270:
            catetoAdyacente = catetoAdyacente * -1

        return catetoOpuesto, catetoAdyacente

    def calcularPocicion(self):
        """
        Ejecuta la logiga de movimiento con las variables
        del jugador y estableciendo la posicion del jugador
        a la proporcionada por los calculos
        """
        catetoOpuesto, catetoAdyacente = self.getCatetos()

        self.dx = catetoAdyacente * self.velocidad
        self.dy = catetoOpuesto * self.velocidad
        x = self.x + self.dx
        y = self.y + self.dy

        self.setPosicion(x, y)

    def update(self):
        """
        Administra las acciones dadas por las teclas presionadas
        actualizando posiciones y estados del jugados
        """
        if not keyPressed:
            self.frenar()
            self.frenarGiro()
            self.calcularPocicion()
            return

        if self.teclas["izquierda"] in self.lista_keys:
            self.girarIzquierda()

        elif self.teclas["derecha"] in self.lista_keys:
            self.girarDerecha()

        else:
            self.frenarGiro()

        if self.teclas["avanzar"] in self.lista_keys:
            self.acelerar()

        else:
            self.frenar()

        self.calcularPocicion()

    def display(self):
        """
        Muestra el jugador y hitbox
        """
        self.hitbox.display()
        stroke(204, 102, 0)
        translate(self.x, self.y)
        rotate(radians(self.angulo + 90))
        triangle(- 10, 20, 0, - 20,   10,  20)
