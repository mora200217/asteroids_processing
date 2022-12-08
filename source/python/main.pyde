from hitbox import Hitbox
from jugador import Jugador

lista_keys = []
class App:
    def __init__(self):
        self.entidades = []
        self.entidades.append(Jugador(20,20,Hitbox(ancho=22,alto=22,visible=True),lista_keys,velocidadMaxima=10))
        
    def draw(self):
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
    app.draw()

def keyPressed(event):
    if key not in lista_keys:
        lista_keys.append(key)

def keyReleased(event):
    if key in lista_keys:
        lista_keys.remove(key)
