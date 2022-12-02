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
    print(h.intersecta(h2))
    h.setPosicion(mouseX, mouseY)  #  sdasssssdsa
    h.display()
