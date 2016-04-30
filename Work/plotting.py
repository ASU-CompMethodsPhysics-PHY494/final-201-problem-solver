import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------------

def plot_time_t_positions(table, positions_plot, plot_index, table_xdims, table_ydims):
    """Plots the positions of all the balls at a given time t
    
    Parameters
    ----------
    table : object
        used to get the positions of the walls and the radii of the balls
    positions_plot : list
        list of arrays of positions of all of the balls at times separated by plot_interval
    plot_index : int
        index of positions_plot to look at
    table_xdims : float
        x dimension extent of the table
    table_ydims : float
        y dimension extent of the table
    """
    num_balls = len(positions_plot[plot_index].T[0])    # gets the number of balls at time t
    
    plt.axes()
    
    # plotting the balls
    for i in range(num_balls):
        plt.gca().add_patch(plt.Circle(positions_plot[plot_index][i], radius=table.ball_radius, color='blue'))
    
    for i in range(len(table.hole_positions)):
        plt.gca().add_patch(plt.Circle(table.hole_positions[i], radius=table.hole_radius, color='darkred'))

    
    # plotting the table walls
    plt.gca().add_patch(plt.Rectangle((table.x_left, table.y_bottom), 100, 200, fc='none'))
    
    plt.axis('scaled')
    plt.show()