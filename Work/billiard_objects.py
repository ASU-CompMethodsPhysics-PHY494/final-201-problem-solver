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
    delta_velocity : array
        change in the x/y velocity before being updated after collision calculations
    status : string
        the status of the ball
    """
    
    def __init__(self, name, mass, radius, position=np.zeros(2, dtype='float64'), velocity=np.zeros(2, dtype='float64')):
        
        self.name = name
        self.position = position
        self.velocity = velocity
        self.delta_velocity = np.zeros_like(self.velocity, dtype='float64')
        self.status = "Present"
        
        if mass > 0:
            self.mass = mass
        else:
            raise ValueError("Mass needs to be positive and nonzero")
        
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Radius needs to be positive and nonzero")
    
    def set_position(self, new_value):
        self.position = new_value
    
    def set_velocity(self, new_value):
        self.velocity = new_value
    
    def add_delta_velocity(self, delta_vx, delta_vy):
        """Adds a component of the change in velocity"""
        self.delta_velocity += np.array([delta_vx, delta_vy], dtype='float64')
    
    def update_velocity(self):
        """Takes the current delta_velocity and adds it to the current velocity, resets delta_velocity back to 0"""
        self.set_velocity(self.velocity + self.delta_velocity)
        self.delta_velocity = np.zeros_like(self.delta_velocity, dtype='float64')
    
    def remove(self):
        self.status = "Removed"
    
       
class Table(object):
    """Contains the dimensions of the table and all its walls
    
    Parameters
    ----------
    x_left : float
        x coordinate of the left wall
    x_right : float
        x coordinate of the right wall
    y_bottom : float
        y coordinate of the bottom wall
    y_top : float
        y coordinate of the top wall
    """
    def __init__(self, xdims, ydims):
        self.x_left = -.5*xdims
        self.x_right = .5*xdims
        self.y_bottom = -.5*ydims
        self.y_top = .5*ydims
    
    
#------------------------------------------------------------------------------------------------------------------------------------------
# Declare the Objects
#------------------------------------------------------------------------------------------------------------------------------------------

def initialize_objects():
    """Initializes and returns a list of all the ball objects"""
    
    cue = Ball('cue', 0.165, 5.7, np.array([0, 50], dtype='float64'))
    ball_1 = Ball('ball 1', .165, 5.7, np.array([-20, 100], dtype='float64'))
    ball_2 = Ball('ball 2', .165, 5.7, np.array([-10, 150], dtype='float64'))
    ball_3 = Ball('ball 3', .165, 5.7, np.array([10, 150], dtype='float64'))
    ball_4 = Ball('ball 4', .165, 5.7, np.array([20, 100], dtype='float64'))
    
    balls = [cue, ball_1, ball_2, ball_3, ball_4]
    
    table = Table(100, 200)
    
    return balls, table