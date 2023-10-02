from classes.Physics import Physics

class Proyectil:
    def __init__(self, physics: Physics = Physics()):
        self.physics = physics

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

    def calculatePositionX(self, time: int): 
        return self.physics.calculatePositionX(self, time, self.initialPosX)
    
    def calculatePositionY(self, time: int):
        return self.physics.calculatePositionY(self, time, self.initialPosY)