from hitbox import Hitbox
from jugador import Jugador

lista_keys = []
class App:
    def __init__(self):
        self.entidades = []
        self.entidades.append(Jugador(20,20,lista_keys))

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

def keyPressed():
    if key not in lista_keys:
        lista_keys.append(key)

def keyReleased():
    if key in lista_keys:
        lista_keys.remove(key)
    
