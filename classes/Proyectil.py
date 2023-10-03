from classes.Physics import Physics

class Proyectil:
    def __init__(self, angle, velocity, physics: Physics = Physics(), start_position: tuple = (0, 0)) -> None:
        self.physics = physics

        self.angle = angle
        self.velocity = velocity
        self.initial_position = start_position
        self.position = start_position
    
    def set_angle(self, angle: int):
        self.angle = angle
    
    def set_velocity(self, velocity: int):
        self.velocity = velocity


    def calculate_position(self, time: int):
        x = self.physics.calculate_position_x(time, self.velocity, self.initial_position[0])
        y = self.physics.calculate_position_y(time, self.velocity, self.initial_position[1])

        return (x, y)