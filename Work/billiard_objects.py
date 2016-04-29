# This module creates the Objects for the balls and the table itself
# PHY 494 - Billiard Simulation Final

import numpy as np

#----------------------------------------------------------------------------------------------------------------------------------
# Define all of the Objects
#----------------------------------------------------------------------------------------------------------------------------------

class Ball(object):
    """ 
    Parameters
    ----------
    name : string
        name of the ball
    position : array
        x/y coordinates of the ball
    velocity : array
        x/y velocity of the ball
    delta_velocity : array
        change in the x/y velocity before being updated after collision calculations
    """
    
    def __init__(self, name, position=np.zeros(2, dtype='float64'), velocity=np.zeros(2, dtype='float64')):
        self.name = name
        self.position = position
        self.velocity = velocity
        self.delta_velocity = np.zeros(2, dtype='float64')

    def set_position(self, new_value):
        self.position = new_value
    
    def set_velocity(self, new_value):
        self.velocity = new_value
        
    def reset_velocity(self):
        self.velocity = np.zeros(2, dtype='float64')
        
    def reset_delta_velocity(self):
        self.delta_velocity = np.zeros(2, dtype='float64')
    
    def add_delta_velocity(self, delta_vx, delta_vy):
        """Adds a component of the change in velocity"""
        self.delta_velocity += np.array([delta_vx, delta_vy], dtype='float64')
    
    def update_velocity(self):
        """Takes the current delta_velocity and adds it to the current velocity, resets delta_velocity back to 0"""
        self.set_velocity(self.velocity + self.delta_velocity)
        self.reset_delta_velocity()

  
class Table(object):
    """Contains the parameters of the table and its holes as well as a list of all active ball objects
    
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
    balls : list
        list of all ball objects that haven't been removed through holes yet
    ball_mass : float
        masses of the balls
    ball_radius : float
        radii of the balls
    holes : array
        array of the positions of all the holes
    hole_radius : float
        radii of the holes
    """
    def __init__(self, xdims, ydims, ball_mass, ball_radius, hole_radius):
        self.x_left = -.5*xdims
        self.x_right = .5*xdims
        self.y_bottom = -.5*ydims
        self.y_top = .5*ydims
        self.balls = []
        self.ball_mass = ball_mass
        self.ball_radius = ball_radius
        
        self.hole_positions = np.array([[self.x_left, self.y_bottom], [self.x_right, self.y_bottom], \
                               [self.x_right, 0], [self.x_right, 0], \
                               [self.x_left, self.y_top], [self.x_right, self.y_top]])
        self.hole_radius = hole_radius
        self.num_holes = len(self.hole_positions.T[0])
    
    def add_balls(self, *balls):
        for ball_i in balls:
            self.balls.append(ball_i)
    
    def remove_ball(self, ball):
        self.balls.remove(ball)

    def reset_balls(self, *balls):
        self.balls = []
    
    def get_ball_positions(self):
        """Creates an array of the positions of all the balls"""
        positions_array = np.zeros([len(self.balls), 2])
        for i, ball_i in enumerate(self.balls):
            positions_array[i] = ball_i.position
        return positions_array
    
    def update_ball_velocities(self):
        for ball in self.balls:
            ball.update_velocity()
    
    def all_removed(self):
        return (len(self.balls) == 0)    # returns True if the balls list is empty
        
        
#----------------------------------------------------------------------------------------------------------------------------------
# Declare the Objects
#----------------------------------------------------------------------------------------------------------------------------------


def create_objects(ball_mass=0.165, ball_radius=5.7, hole_radius = 11.4, table_xdims=100, table_ydims=200):
    """Creates and returns a list of all the ball objects and the table object
    
    Parameters
    ----------
    ball_mass : float
        mass to set the balls to
    ball_radius : float
        radius to set the balls to
    hole_radius : float
        radius to set the holes to
    table_xdims : float
        x dimension extent of the table
    table_ydims : float
        y dimension extent of the table
    
    Returns
    -------
    table : object
    starting_balls : list
        list of balls; used for repopulating the table after a simulation
    """
    #ball objects and table object
    cue = Ball('cue')
    ball_1 = Ball('ball 1')
    ball_2 = Ball('ball 2')
    ball_3 = Ball('ball 3')
    ball_4 = Ball('ball 4')
    
    table = Table(100, 200, ball_mass, ball_radius, hole_radius)
    
    table.add_balls(cue, ball_1, ball_2, ball_3, ball_4)
    starting_balls = table.balls
    
    return table, starting_balls