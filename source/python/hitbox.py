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