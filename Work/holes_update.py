# This module creates the Objects for the balls, the balls on table, and the table itself
# PHY 494 - Billiard Simulation Final

import numpy as np

#-------------------------------------------------------------------------------------------------------------------------------------------
# Define all of the Objects
#-------------------------------------------------------------------------------------------------------------------------------------------

# Define a Ball
class Ball(object):
    def __init__(self, name, radius, position, mass = .165, velocity):
        
        self.name = name
        self.position = position
        self.velocity = None
        
        if mass >= 0:
            self.mass = mass
        else:
            raise ValueError("Mass needs to be positive and nonzero")
        
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError("Radius needs to be positive and nonzero")
    
    def get_name(self):
        return self.name
    
    def get_mass(self):
        return self.mass
    
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity
    
    def set_position(self,pos):
        self.position = pos
        
    def set_velocity(self,vel):
        self.velocity = vel
        

# Define the Table
class Table(object):
    
    def __init__(self, L,hole_radius):
        self.length = L
        self.holes = np.array([[0,0],[0, L],[0, 2*L],[L, 2*L],[L, L],[L, 0]])
        self.balls = []
        self.hole_radius = hole_radius
        
    def add_ball(self, ball):
        if type(ball) is list:
            for b in ball:
                self.balls.append(b)
        else:
            self.balls.append(ball)
            
    def get_holes(self):
        return self.holes
    
    def check_positions(self):
        for b in self.balls:
            for h in self.holes:
                marker = h - b.position
                if np.linalg.norm(marker) < self.hole_radius:
                    self.balls.remove(b)
                    
    def is_empty(self):
        return len(self.balls) == 0