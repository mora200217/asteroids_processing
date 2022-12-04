from hitbox import Hitbox
from jugador import Jugador

class App:
    def __init__(self):
        self.entidades = []
        self.entidades.append(Jugador(20,20))
        self.h = Hitbox(visible=True)
        self.h2 = Hitbox(visible=True)

    def update(self):
        background(255)
        for entidad in self.entidades:
            entidad.update()
        
        for entidad in self.entidades:
            entidad.display()

def setup():
    global app
    app = App()
    size(640, 360)

def draw():
    app.update()
