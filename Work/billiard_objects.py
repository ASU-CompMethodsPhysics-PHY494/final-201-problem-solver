# This module creates the Objects for the balls, the balls on table, and the table itself
# PHY 494 - Billiard Simulation Final

import numpy as np

#------------------------------------------------------------------------------------------------------------------------------------------
# Define all of the Objects
#------------------------------------------------------------------------------------------------------------------------------------------

# Define a Ball
class Ball(object):
    """ 
    Parameters
    ----------
    name : string
        name of the ball
    mass : float
        mass of the ball
    radius : float
        radius of the ball
    position : array
        x/y coordinates of the ball
    velocity : array
        x/y velocity of the ball
    status : string
        the status of the ball
    """
    
    def __init__(self, name, mass, radius, position, velocity):
        
        self.name = name
        self.position = position
        self.velocity = velocity
        self.status = "Present"
        
        if mass > 0:
            self.mass = mass
        else:
            raise ValueError("Mass needs to be positive and nonzero")
        
        if radius > 0:
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
    
    def get_status(self):
        return self.status
    
    def remove(self, new_value):
        self.status = "Removed"
    
    
class Holes(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        return (self.x, self.y)


        
class Table(object):
    """Contains all of the relevant parameters of the table
    
    Parameters
    ----------
    """
    def __init__(self):
        self.holes = []
        
    def add_holes(self, addition):
        self.holes.append(addition)
        
    def get_holes(self):
        return self.holes
    
    
class Table_Balls(object):
    
    def __init__(self):
        self.balls = []
        
    def add_balls(self, addition):
        self.balls.append(addition)
        
    def get_balls(self):
        return self.balls
    
    def check_position(self, holes = Table.get_holes):
        for i,m in enumerate(holes):
            for j,t in enumerate(self.position):
                if t == m:
                    print("\'{}\' fell in hole.".format(m.get_name()))
                    self.position.remove(t)


#------------------------------------------------------------------------------------------------------------------------------------------
# Declare the Objects
#------------------------------------------------------------------------------------------------------------------------------------------

cue = Ball('cue', 0.165, 5.7, np.array([50, 50]))
ball_1 = Ball('ball 1', .165, 5.7, np.array([30, 100]))
ball_2 = Ball('ball 2', .165, 5.7, np.array([40, 150]))
ball_3 = Ball('ball 3', .165, 5.7, np.array([60, 150]))
ball_4 = Ball('ball 4', .165, 5.7, np.array([70, 100]))

balls = Table_Balls()
balls.add_balls(cue)
balls.add_balls(ball_1)
balls.add_balls(ball_2)
balls.add_balls(ball_3)
balls.add_balls(ball_4)