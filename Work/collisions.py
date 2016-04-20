def wall_collision(positions, velocities, radii, walls):
    """Takes the current positions and velocities of the particles. If they hit a wall then reverse the velocity for that direction.
    Only applies to rectangular boundaries
    
    Parameters
    ----------
    positions : array
        x and y coordinates of the particles
    velocities : array
        x and y velocities of the particles
    radii : array
        the radii of the particles
    walls : array
        array defining the walls for rectangular boundaries
    
    Returns
    -------
    velocities : array
        updates x and y velocities of the particles
    """
    # coordinates of the edges of the wall
    wall_left = ??
    wall_right = ??
    wall_top = ??
    wall_bottom = ??
    
    n = positions.shape[0]    # number of particles
    
    for i in range(n):
        # if the current position +- the radius falls outside of the boundaries then reverse the velocity
        if ((positions[i, 0] - radii[i]) < wall_left) or ((positions[i, 0] + radii[i]) > wall_right):
            velocities[i, 0] *= -1
        if ((positions[i, 1] - radii[i]) < wall_bottom) or ((positions[i, 1] + radii[i]) > wall_top):
            velocities[i, 1] *= -1
    
    return velocities

def ball_collision(positions, velocities, radii, masses):
    """Takes the current positions and velocities of the particles. If their radii overlap then calculate their new velocities.
    
    Parameters
    ----------
    positions : array
        x and y coordinates of the particles
    velocities : array
        x and y velocities of the particles
    radii : array
        the radii of the particles
    masses : array
        the masses of the particles
    
    Returns
    -------
    velocities : array
        updates x and y velocities of the particles
    """
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
                
                # intermediate values
                vi_left_part = (vi * np.cos(theta_i - phi) * (masses[i] - masses[j]) + \
                                   2 * masses[j] * vj * np.cos(theta_j - phi)) / (masses[i] + masses[j])
                vi_right_part = vi * np.sin(theta_i - phi)
                vj_left_part = (vj * np.cos(theta_j - phi) * (masses[j] - masses[i]) + \
                                   2 * masses[i] * vi * np.cos(theta_i - phi)) / (masses[i] + masses[j])
                vj_right_part = vj * np.sin(theta_j - phi)
                
                #final calculation
                velocities[i, 0] = vi_left_part * np.cos(phi) + vi_right_part * np.cos(phi + .5 * np.pi)
                velocities[i, 1] = vi_left_part * np.sin(phi) + vi_right_part * np.sin(phi + .5 * np.pi)
                velocities[j, 0] = vj_left_part * np.cos(phi) + vj_right_part * np.cos(phi + .5 * np.pi)
                velocities[j, 1] = vj_left_part * np.sin(phi) + vj_right_part * np.sin(phi + .5 * np.pi)
    
    return velocities