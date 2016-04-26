import numpy as np

def new_velocities(balls, table):
    """Calculates the change in velocities due to each collision and sums them up to find the new velocities
    
    Parameters
    ----------
    balls : list
        contains all the ball objects with the following parameters
        
        masses : array
            masses of the balls
        radii : array
            radii of the balls
        positions : array
            x/y coordinates of the balls
        velocities : array
            x/y velocities of the balls
    
    table : object
        contains the dimensions of the table
    """
    delta_velocities_total = wall_collision(balls, table) + ball_collision(balls)
    
    for i, ball_i in enumerate(balls):
        new_velocity = ball_i.velocity + delta_velocities_total[i]
        ball_i.set_velocity(new_velocity)
    
        
def wall_collisions(balls, table):
    """Takes the current positions and velocities of the particles. If they hit a wall then reverse the velocity for that direction.
    Only applies to rectangular boundaries
    """
    for ball_i in balls:
        if ball_i.status is "Removed":    # only calculates for balls that aren't removed
            continue
        
        # if the current position +- the radius falls outside of the boundaries then
        # add 2*velocity(in the x or y direction ) in the opposite direction to the wall
        # absolute value is used to ensure the correct direction

        delta_vx, delta_vy = 0, 0
        
        if (ball_i.position[0] - ball_i.radius) < table.x_left:
            delta_vx = 2*np.abs(ball_i.velocity[0])
        if (ball_i.position[0] + ball_i.radius) > table.x_right:
            delta_vx = -2*np.abs(ball_i.velocity[0])
        if (ball_i.position[1] - ball_i.radius) < table.y_bottom:
            delta_vy = 2*np.abs(ball_i.velocity[1])
        if (ball_i.position[1] + ball_i.radius) > table.y_top:
            delta_vy = -2*np.abs(ball_i.velocity[1])
        ball_i.add_delta_velocity(delta_vx, delta_vy)

def ball_collisions(balls):
    """Takes the current positions and velocities of the balls. If their radii overlap then calculate their new velocities.
    
    Parameters
    ----------
    masses : array
        masses of the balls
    radii : array
        radii of the balls
    positions : array
        x/y coordinates of the balls
    velocities : array
        x/y velocities of the balls

    
    Returns
    -------
    delta_velocities : array
        change in x and y velocities of the particles due to collisions between balls
    """
    for i, ball_i in enumerate(balls):
        for j, ball_j in enumerate(balls[i+1:]):    # avoids calculating for the same collision twice
            if ball_i.status is "Removed":    # only calculates for balls that aren't removed
                continue
            
            d_sep = np.sqrt(np.sum((ball_i.position-ball_j.position)**2))
            if d_sep < (ball_i.radius + ball_j.radius):    # the collision check
                # formulas taken from https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional
                
                # velocity magnitude and angles
                vi = np.sqrt(np.sum((ball_i.velocity)**2))
                vj = np.sqrt(np.sum((ball_j.velocity)**2))
                theta_i = np.arctan2(ball_i.velocity[1], ball_i.velocity[0])
                theta_j = np.arctan2(ball_j.velocity[1], ball_j.velocity[0])
                phi = np.arctan2((ball_j.position[1] - ball_i.position[1]), (ball_j.position[0] - ball_i.position[0]))
                
                # intermediate values, the values that don't change between each vi and vj calculation
                vi_left_part = (vi * np.cos(theta_i - phi) * (ball_i.mass - ball_j.mass) + \
                                   2 * ball_j.mass * vj * np.cos(theta_j - phi)) / (ball_i.mass + ball_j.mass)
                vi_right_part = vi * np.sin(theta_i - phi)
                vj_left_part = (vj * np.cos(theta_j - phi) * (ball_j.mass - ball_i.mass) + \
                                   2 * ball_i.mass * vi * np.cos(theta_i - phi)) / (ball_i.mass + ball_j.mass)
                vj_right_part = vj * np.sin(theta_j - phi)
                
                #final calculation
                delta_vx_i = vi_left_part * np.cos(phi) + vi_right_part * np.cos(phi + .5 * np.pi) - ball_i.velocity[0]
                delta_vy_i = vi_left_part * np.sin(phi) + vi_right_part * np.sin(phi + .5 * np.pi) - ball_i.velocity[1]
                delta_vx_j = vj_left_part * np.cos(phi) + vj_right_part * np.cos(phi + .5 * np.pi) - ball_j.velocity[0]
                delta_vy_j = vj_left_part * np.sin(phi) + vj_right_part * np.sin(phi + .5 * np.pi) - ball_j.velocity[1]
                ball_i.add_delta_velocity(delta_vx_i, delta_vy_i)
                ball_j.add_delta_velocity(delta_vx_j, delta_vy_j)