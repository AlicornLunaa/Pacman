from graphics import *
class Food(object):
    def __init__(self, x, y, color, activeColor, window):
        self.x = x
        self.y = y
        self.color = color
        self.active = activeColor
        self.window = window
        self.f = Rectangle(Point(self.x, self.y), Point(self.x + 12, self.y + 12))
        self.drawFood()
    def drawFood(self):
        self.f.setFill(self.color)
        self.f.setActiveFill(self.color)
        self.f.draw(self.window)
    def undrawFood(self):
        self.f.undraw()
    def changeFill(self, color):
        self.color = color
    def moveFood(self, direction):
        if direction.lower() == "n":
            self.y -= 20
            self.f = Rectangle(Point(self.x, self.y), Point(self.x + 12, self.y + 12))
            self.drawFood()

        elif direction.lower() == "e":
            self.x += 20
            self.f = Rectangle(Point(self.x, self.y), Point(self.x + 12, self.y + 12))
            self.drawFood()

        elif direction.lower() == "s":
            self.y += 20
            self.f = Rectangle(Point(self.x, self.y), Point(self.x + 12, self.y + 12))
            self.drawFood()

        elif direction.lower() == "w":
            self.x -= 20
            self.f = Rectangle(Point(self.x, self.y), Point(self.x + 12, self.y + 12))
            self.drawFood()
    def eaten(self, pacmanX, pacmanY):
        if self.x < pacmanX + 39 and self.x + 12 > pacmanX and self.y < pacmanY + 39 and self.y + 12 > pacmanY:
            return True

        return False