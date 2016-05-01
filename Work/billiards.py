import billiard_objects
import collisions
import numpy as np

#----------------------------------------------------------------------------------------------------------------------------------

def initialize_table(table, starting_balls, cue_velocity):
    """
    Takes the ball objects and places them in their starting positions.
    Sets all velocities and delta_velocities to 0. Gives the cue ball the input velocity.
    Resets the balls list in the table object
    
    Parameters
    ----------
    table : object
    starting_balls : list
        list of all ball objects, must contain 5 or less
    cue_velocity : array
        two valued array of the x and y velocity to give the cue
    """
    for ball_i in starting_balls:
        ball_i.reset_velocity()
        ball_i.reset_delta_velocity()
    
    starting_balls[0].set_name("cue")
    starting_balls[0].set_position(np.array([0, -50], dtype='float64'))
    starting_balls[0].set_velocity(cue_velocity)    # overwrites the reset above
    
    for i, ball in enumerate(starting_balls[1:]):    # names all balls 1-4
        ball.set_name("ball " + str(i))
        
    starting_balls[1].set_position(np.array([-20, 0], dtype='float64'))
    starting_balls[2].set_position(np.array([-10, 50], dtype='float64'))
    starting_balls[3].set_position(np.array([10, 50], dtype='float64'))
    starting_balls[4].set_position(np.array([20, 0], dtype='float64'))
    
    table.set_balls_list(starting_balls[:])
    
    
def speed_to_velocity(break_speed, theta_degrees):
    """Converts the break speed and launch angle to x and y components of velocity. Theta in taken degrees"""
    theta_radians = theta_degrees * np.pi / 180
    vx = break_speed * np.cos(theta_radians)
    vy = break_speed * np.sin(theta_radians)
    return np.array([vx, vy], dtype='float64')
    

def move_balls(table, dt):
    """Takes the current velocities of the balls and moves them based on the value of dt"""
    for ball_i in table.balls:
        new_position = ball_i.position + ball_i.velocity * dt
        ball_i.set_position(new_position)
    
    
def ball_removal(table):
    """Checks the positions of all balls and holes, removes any balls that fall within the radius of any hole"""
    for ball_i in table.balls:
        for j in range(table.num_holes):
            d_sep = np.sqrt(np.sum((ball_i.position-table.hole_positions[j])**2))    # calculates the separation distance
            if (d_sep + table.ball_radius) < table.hole_radius:
                table.remove_ball(ball_i)
    
    
def single_simulation(table, starting_balls, break_speed, theta, dt, sim_time_max, plot_interval):
    """Runs a single simulation with the ball and table objects, launching the cue ball at break_speed at angle theta
    
    Parameters
    ----------
    table : object
        contains the parameters of the table
    starting_balls : list
        list of ball objects to run the simulation with.
        only works for balls with names "cue", "ball 1", "ball 2", "ball 3", or "ball 4"
    break_speed : float
        the initial speed of the cue ball
    theta : float
        the initial angle the cue ball is sent at
    dt : float
        the time step between calculations
    sim_time_max : float
        max time to run the simulation for
    plot_interval : float
        time between writing the ball positions out
    
    Returns
    -------
    positions_plot : list
        list of arrays of positions of all of the balls at times separated by plot_interval
    """
    # initialization
    cue_velocity = speed_to_velocity(break_speed, theta)
    initialize_table(table, starting_balls, cue_velocity)
    
    positions_plot = []    # made as a list because the dimensions can change in time if the balls get removed
    t_interval = int(plot_interval/dt)
    
    t_steps = 0
    max_t_steps = int((sim_time_max/dt))
    for t in range(max_t_steps):
        if (t%t_interval) == 0:
            positions_plot.append(table.get_ball_positions())
        move_balls(table, dt)
        ball_removal(table)
        if table.all_removed() or table.all_stopped(10):    # checks if the sum of speeds is 0 up to 10 decimals
            break
        collisions.wall_collisions(table)
        collisions.ball_collisions(table)
        table.update_ball_velocities()
        t_steps += 1
    
    print("Simulation ended after {0} seconds with {1} steps. {2} balls remain on the table." \
          .format(t_steps * dt, t_steps, len(table.balls)))
    
    return positions_plot