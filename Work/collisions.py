import numpy as np

#----------------------------------------------------------------------------------------------------------------------------------

def wall_collisions(table):
    """Takes the current positions and velocities of the balls.
    If they hit a wall then add 2x the velocity in the opposite direction that it hits to its delta_velocity value.
    """
    for ball_i in table.balls:
        
        # if the current position +- the radius falls outside of the boundaries then
        # add 2*velocity(in the x or y direction ) in the opposite direction to the wall
        # absolute value is used to ensure the correct direction

        delta_vx, delta_vy = 0, 0
        
        if (ball_i.position[0] - table.ball_radius) < table.x_left:
            delta_vx = 2*np.abs(ball_i.velocity[0])
        if (ball_i.position[0] + table.ball_radius) > table.x_right:
            delta_vx = -2*np.abs(ball_i.velocity[0])
        if (ball_i.position[1] - table.ball_radius) < table.y_bottom:
            delta_vy = 2*np.abs(ball_i.velocity[1])
        if (ball_i.position[1] + table.ball_radius) > table.y_top:
            delta_vy = -2*np.abs(ball_i.velocity[1])
        ball_i.add_delta_velocity(delta_vx, delta_vy)

        
def ball_collisions(table):
    """Takes the current positions and velocities of the balls. If 
    their radii overlap then calculate their new velocities.
    Updates the balls delta_velocity values at the end of the calculation
    """
    for i, ball_i in enumerate(table.balls):
        for j, ball_j in enumerate(table.balls[i+1:]):    # avoids calculating for the same collision twice

            d_sep = np.sqrt(np.sum((ball_i.position-ball_j.position)**2))
            if d_sep < (table.ball_radius + table.ball_radius):    # the collision check
                # formulas taken from https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional
                
                # velocity magnitude and angles
                vi = np.sqrt(np.sum((ball_i.velocity)**2))
                vj = np.sqrt(np.sum((ball_j.velocity)**2))
                theta_i = np.arctan2(ball_i.velocity[1], ball_i.velocity[0])
                theta_j = np.arctan2(ball_j.velocity[1], ball_j.velocity[0])
                phi = np.arctan2((ball_j.position[1] - ball_i.position[1]), (ball_j.position[0] - ball_i.position[0]))
                
                # intermediate values, the values that don't change between each vi and vj calculation
                vi_left_part = vj * np.cos(theta_j - phi)
                vi_right_part = vi * np.sin(theta_i - phi)
                vj_left_part = vi * np.cos(theta_i - phi)
                vj_right_part = vj * np.sin(theta_j - phi)
                
                #final calculation
                delta_vx_i = vi_left_part * np.cos(phi) + vi_right_part * np.cos(phi + .5 * np.pi) - ball_i.velocity[0]
                delta_vy_i = vi_left_part * np.sin(phi) + vi_right_part * np.sin(phi + .5 * np.pi) - ball_i.velocity[1]
                delta_vx_j = vj_left_part * np.cos(phi) + vj_right_part * np.cos(phi + .5 * np.pi) - ball_j.velocity[0]
                delta_vy_j = vj_left_part * np.sin(phi) + vj_right_part * np.sin(phi + .5 * np.pi) - ball_j.velocity[1]
                ball_i.add_delta_velocity(delta_vx_i, delta_vy_i)
                ball_j.add_delta_velocity(delta_vx_j, delta_vy_j)