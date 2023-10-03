from classes.Physics import Physics

class Proyectil:
    def __init__(self, angle, velocity, physics: Physics = Physics(), start_position: tuple = (0, 0)) -> None:
        self.physics = physics

        self.angle = angle
        self.velocity = velocity
        self.initial_position = start_position
        self.position = start_position

        self.time = 0

    
    def set_angle(self, angle: int):
        self.angle = angle

    
    def set_velocity(self, velocity: int):
        self.velocity = velocity


    def reset_time(self):
        self.time = 0


    def add_time(self):
        self.time += 0.1


    def calculate_position_on_proyectile_time(self):
        return self.calculate_position(self.time)


    def calculate_position(self, time: int):
        x = self.physics.calculate_position_x(time, self.velocity, self.angle, self.initial_position[0])
        y = self.physics.calculate_position_y(time, self.velocity, self.angle, self.initial_position[1])

        return (x, y)