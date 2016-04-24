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
    
    def __init__(self, name, mass, radius, position, velocity=0):
        
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
        
    def set_velocity(self, new_value):
        self.velocity = new_value
   
    def remove(self):
        self.status = "Removed"
    
    def unremove(self):
        self.status = "Present"
    
    
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
    """Contains multiple balls"""
    def __init__(self):
        self.table_balls = []
        
    def add_ball(self, addition):
        self.table_balls.append(addition)
        
    def get_balls(self):
        return self.table_balls
    
    def names(self):
        names = []
        for ball in self.table_balls:
            names.append(ball.name)
        return names
    
    def masses(self):
        masses = []
        for ball in self.table_balls:
            masses.append(ball.mass)
        return masses
    
    def radii(self):
        radii = []
        for ball in self.table_balls:
            radii.append(ball.radius)
        return radii
    
    def positions(self):
        positions = []
        for ball in self.table_balls:
            positions.append(ball.position)
        return positions
    
    def velocities(self):
        velocities = []
        for ball in self.table_balls:
            velocities.append(ball.velocity)
        return velocities
    
    def set_velocities(self, new_velocities):
        if new_velocities[0] != self.table_balls.num_balls():
            raise ValueError("The number of values for velocities must equal the number of balls")
        for i, ball_i in enumerate(self.table_balls):
            ball_i.set_velocity(new_values[i])
    
    def statuses(self):
        statuses = []
        for ball in enumerate(self.table_balls):
            statuses.append(ball.status)
        return statuses
    
    def num_balls(self):
        return len(self.table_balls)

#------------------------------------------------------------------------------------------------------------------------------------------
# Declare the Objects
#------------------------------------------------------------------------------------------------------------------------------------------

cue = Ball('cue', 0.165, 5.7, np.array([50, 50]))
ball_1 = Ball('ball 1', .165, 5.7, np.array([30, 100]))
ball_2 = Ball('ball 2', .165, 5.7, np.array([40, 150]))
ball_3 = Ball('ball 3', .165, 5.7, np.array([60, 150]))
ball_4 = Ball('ball 4', .165, 5.7, np.array([70, 100]))

balls = Table_Balls()
balls.add_ball(cue)
balls.add_ball(ball_1)
balls.add_ball(ball_2)
balls.add_ball(ball_3)
balls.add_ball(ball_4)