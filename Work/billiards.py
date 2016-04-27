import billiard_objects
import collisions
import numpy as np

#---------------------------------------------------------------------------------------------------------------------------------------------
# parameters
ball_mass = 0.165
ball_radius = 5.7
table_xdims = 100
table_ydims = 200

#---------------------------------------------------------------------------------------------------------------------------------------------
# creating the objects to use
balls, table = billiard_objects.create_objects(ball_mass, ball_radius, table_xdims, table_ydims)

#---------------------------------------------------------------------------------------------------------------------------------------------

def initialize_balls(balls, cue_velocity):
    """
    Takes the ball objects and places them in their starting positions.
    Sets all the balls velocities to 0 except for the cue which takes on the velocity given.
    Also sets all delta_velocities to 0 to avoid carrying its value over between simulations.
    
    Parameters
    ----------
    balls : list
        list of all ball objects
        only affects balls with names "cue", "ball 1", "ball 2", "ball 3", or "ball 4"
    cue_velocity : array
        two valued array of the x and y velocity to give the cue
    """"
    for ball_i in balls:
        ball_i.reset_delta_velocity()
        ball_i.reset_velocity()
            
        if ball_i.name is "cue":
            ball_i.set_position(np.array([0, -50], dtype='float64'))
            ball_i.set_velocity(cue_velocity)    # overwrites the reset above
            
        if ball_i.name is "ball 1":
            ball_i.set_position(np.array([-20, 0], dtype='float64'))
            
        if ball_i.name is "ball 2":
            ball_i.set_position(np.array([-10, 50], dtype='float64'))
            
        if ball_i.name is "ball 3":
            ball_i.set_position(np.array([10, 50], dtype='float64'))
            
        if ball_i.name is "ball 4":
            ball_i.set_position(np.array([20, 0], dtype='float64'))