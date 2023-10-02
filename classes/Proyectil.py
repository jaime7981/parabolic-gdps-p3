from .Wind import Wind

class Proyectil:
    def __init__(self):
        self.angle = 0
        self.velocityX = 0
        self.velocityY = 0
        self.initialPosX = 0
        self.initialPosY = 0
        self.positionX = 0
        self.positionY = 0
    
    def setAngle(self, angle: int):
        self.angle = angle
    
    def setVelocityX(self, velocity: int):
        self.velocityX = velocity
    
    def setVelocityY(self, velocity: int):
        self.velocityY = velocity

    #x(t) = ½ axt2 + v0xt + x0, retorna la posicion del proyectil en X para despues graficar
    def calculatePositionX(self, time: int, wind: Wind): 
        self.positionX = 1/2*(wind.magnitud*time**2) + (self.velocityX*time) + self.initialPosX
        return self.positionX
    
    #y(t) = -½ gt2 + v0yt + y0, retorna la posicion del proyectil en Y para despues graficar
    def calculatePositionY(self, time: int, wind: Wind):
        self.positionY = -1/2*(wind.gravity*time**2) + (self.velocityY*time) + self.initialPosY
        return self.positionY