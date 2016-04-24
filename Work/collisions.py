import numpy as np

def new_velocities(balls, table):
    """Calculates the change in velocities due to each collision and sums them up to find the new velocities
    
    Parameters
    ----------
    balls : object
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
        contains the dimensions of the table and the positions of the walls
    
    
    Returns
    -------
    velocities : array
        updates the velocities for each ball the new velocities after calculating each collision
    """
    # old velocities plus the changes due to the collisions with the walls and with other balls
    new_velocities = balls.velocities() + wall_collision(balls, table) + ball_collision(balls)
    
    balls.set_velocities(new_velocities)

def wall_collision(balls, table):
    """Takes the current positions and velocities of the particles. If they hit a wall then reverse the velocity for that direction.
    Only applies to rectangular boundaries
    
    Parameters
    ----------
    radii : array
        radii of the balls
    positions : array
        x/y coordinates of the balls
    velocities : array
        x/y velocities of the balls
    walls : ??
    
    Returns
    -------
    delta_velocities : array
        change in x and y velocities of the particles due to collisions with the walls
    """
    positions = balls.positions
    velocities = balls.velocities
    radii = balls.radii
    
    
    # coordinates of the edges of the wall
    wall_left = ??
    wall_right = ??
    wall_top = ??
    wall_bottom = ??
    
    delta_velocities = np.zeros_like(velocities)
    n = positions.shape[0]    # number of particles
    
    for i in range(n):
        # if the current position +- the radius falls outside of the boundaries then
        # add 2*velocity(in the x or y direction ) in the opposite direction to the wall
        raise NotImplemented("Need to add in holes to walls")
        if (positions[i, 0] - radii[i]) < wall_left:
            delta_velocities[i, 0] = 2*np.abs(velocities[i, 0])
        if (positions[i, 0] + radii[i]) > wall_right:
            delta_velocities[i, 0] = -2*np.abs(velocities[i, 0])
        if (positions[i, 1] - radii[i]) < wall_bottom:
            delta_velocities[i, 1] = 2*np.abs(velocities[i, 1])
        if (positions[i, 1] + radii[i]) > wall_top:
            delta_velocities[i, 1] = -2*np.abs(velocities[i, 1])
    
    return delta_velocities

def ball_collision(balls):
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
    positions = balls.positions
    velocities = balls.velocities
    radii = balls.radii
    masses = balls.masses
    
    delta_velocities = np.zeros_like(velocities)
    n = positions.shape[0]
    
    for i in range(n):
        for j in range(i+1, n):    # avoids calculating for the same collision twice
            d_sep = np.sqrt(np.sum((positions[i]-positions[j])**2))
            if d_sep < (radii[i] + radii[j]):    # the collision check
                # formulas taken from https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional
                
                # velocity magnitude and angles
                vi = np.sqrt(np.sum((velocities[i])**2))
                vj = np.sqrt(np.sum((velocities[j])**2))
                theta_i = np.arctan2(velocities[i, 1], velocities[i, 0])
                theta_j = np.arctan2(velocities[j, 1], velocities[j, 0])
                phi = np.arctan2((positions[j, 1] - positions[i, 1]), (positions[j, 0] - positions[i, 0]))
                
                # intermediate values, the values that don't change between each vi and vj calculation
                vi_left_part = (vi * np.cos(theta_i - phi) * (masses[i] - masses[j]) + \
                                   2 * masses[j] * vj * np.cos(theta_j - phi)) / (masses[i] + masses[j])
                vi_right_part = vi * np.sin(theta_i - phi)
                vj_left_part = (vj * np.cos(theta_j - phi) * (masses[j] - masses[i]) + \
                                   2 * masses[i] * vi * np.cos(theta_i - phi)) / (masses[i] + masses[j])
                vj_right_part = vj * np.sin(theta_j - phi)
                
                #final calculation
                delta_velocities[i, 0] = vi_left_part * np.cos(phi) + vi_right_part * \
                                             np.cos(phi + .5 * np.pi) - velocities[i, 0]
                delta_velocities[i, 1] = vi_left_part * np.sin(phi) + vi_right_part * \
                                             np.sin(phi + .5 * np.pi) - velocities[i, 1]
                delta_velocities[j, 0] = vj_left_part * np.cos(phi) + vj_right_part * \
                                             np.cos(phi + .5 * np.pi) - velocities[j, 0]
                delta_velocities[j, 1] = vj_left_part * np.sin(phi) + vj_right_part * \
                                             np.sin(phi + .5 * np.pi) - velocities[j, 1]
    
    return delta_velocities