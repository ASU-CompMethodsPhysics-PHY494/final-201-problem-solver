import billiard_objects
import collisions
import numpy as np

#----------------------------------------------------------------------------------------------------------------------------------
# parameters
ball_mass = 0.165
ball_radius = 5.7
hole_radius = 11.4
table_xdims = 100
table_ydims = 200

dtheta = 30
break_speed = 100
dt = .05
max_sim_time = 500

#----------------------------------------------------------------------------------------------------------------------------------
# creating the objects to use
table = billiard_objects.create_objects(ball_mass, ball_radius, hole_radius, table_xdims, table_ydims)

#----------------------------------------------------------------------------------------------------------------------------------

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
        ball_i.reset_velocity()
        ball_i.reset_delta_velocity()
            
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
    
    
def speed_to_velocity(break_speed, theta):
    """Converts the break speed and launch angle to x and y components of velocity"""
    vx = break_speed * np.cos(theta)
    vy = break_speed * np.sin(theta)
    return np.array([vx, vy], dtype='float64')
    
    
def ball_removal(table):
	"""Checks the positions of all balls and holes, removes any balls that fall within the radius of any hole"""
	for ball_i in table.balls:
		for j in range(table.num_holes):
			d_sep = np.sqrt(np.sum(ball_i.position-table.hole_positions[j])**2)    # calculates the separation distance
			if (d_sep + ball_i.radius) < table.hole_radius:
				table.remove_ball(ball_i)
	
	
def single_simulation(balls, table, break_speed, theta, dt, max_sim_time):
    """Runs a single simulation with the ball and table objects, launching the cue ball at break_speed at angle theta
    
    Parameters
    ----------
    balls : list
        list of all ball objects
    table : object
        contains the parameters of the table
    break_speed : float
        the initial speed of the cue ball
    theta : float
        the initial angle the cue ball is sent at
    dt : float
        the time step between calculations
    max_sim_time : float
        max time to run the simulation for, ends if the current time is greater than max_sim_time
    """
    # initialization
    cue_velocity = speed_to_velocity(break_speed, theta)
    initialize_balls(balls, cue_velocity)
    
    t_steps = int(max_sim_time / dt) + 1    # +1 to include first and last step
    