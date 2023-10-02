from classes.enums import Difficulty
from random import randint


class Physics():
    def __init__(self, difficulty: Difficulty = Difficulty.easy) -> None:
        self.gravity = 9.8
        self.magnitud = self.setWindMagnitud(difficulty)


    def setWindMagnitud(self, difficulty: Difficulty = Difficulty.none):
        if difficulty == Difficulty.none:
            self.magnitud = 0

        if difficulty == Difficulty.easy:
            self.magnitud = randint(1, 5)

        if difficulty == Difficulty.medium:
            self.magnitud = randint(5, 10)

        if difficulty == Difficulty.hard:
            self.magnitud == randint(10, 20)


    def setAngle(self, angle: int):
        self.angle = angle
    

    def setVelocityX(self, velocity: int):
        self.velocityX = velocity
    

    def setVelocityY(self, velocity: int):
        self.velocityY = velocity


    #x(t) = ½ axt2 + v0xt + x0, retorna la posicion del proyectil en X para despues graficar
    def calculatePositionX(self, time: int, initialPosX:int = 0): 
        positionX = 1/2*(self.magnitud*time**2) + (self.velocityX*time) + initialPosX
        return positionX
    

    #y(t) = -½ gt2 + v0yt + y0, retorna la posicion del proyectil en Y para despues graficar
    def calculatePositionY(self, time: int, initialPosY:int = 0):
        positionY = -1/2*(self.gravity*time**2) + (self.velocityY*time) + initialPosY
        return positionY