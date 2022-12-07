# main.pyde
from hitbox import Hitbox


def setup():
    global h
    global h2
    size(640, 360)
    h = Hitbox(visible = True)
    h2 = Hitbox(visible = True)


def draw():
    background(255)
    
    h2.display()
    h.setPosicion(mouseX, mouseY)
    h.display()
    print(h.intersecta(h2))
