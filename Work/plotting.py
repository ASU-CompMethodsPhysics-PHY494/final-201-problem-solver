import numpy as np
import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------------------------------------

def plot_time_t_positions(table, positions_plot, plot_index, ball_color='blue', hole_color='darkred'):
    """Plots the positions of all the balls at a given time t
    
    Parameters
    ----------
    table : object
        used to get the positions of the walls and holes and the radii of the balls and holes
    positions_plot : list
        list of arrays of positions of all of the balls at times separated by plot_interval
    plot_index : int
        index of positions_plot to look at
    ball_color : string
        color to make the balls in the plot
    hole_color : string
        color to make the holes in the plot
    """
    num_balls = len(positions_plot[plot_index].T[0])    # gets the number of balls at the time of the plot index

    fig, ax = plt.subplots()

    # hole patches
    for i in range(len(table.hole_positions)):
        plt.gca().add_patch(plt.Circle(table.hole_positions[i], radius=table.hole_radius, color=hole_color))
    
    # ball patches
    for i in range(num_balls):
        ax.add_patch(plt.Circle(positions_plot[plot_index][i], radius=table.ball_radius, color=ball_color))
    
    # rectangle patches for turning the holes to partial circles and for the table boundaries
    rad = table.hole_radius+5    # size to make the rectangles extend outside the table so that they overlap the holes
    ax.add_patch(plt.Rectangle((table.x_left-rad, table.y_bottom-rad), rad, table.ydims+2*rad, fc='white', ec='none'))
    ax.add_patch(plt.Rectangle((table.x_right, table.y_bottom-rad), rad, table.ydims+2*rad, fc='white', ec='none'))
    ax.add_patch(plt.Rectangle((table.x_left-rad, table.y_bottom-rad), table.xdims+2*rad, rad, fc='white', ec='none'))
    ax.add_patch(plt.Rectangle((table.x_left-rad, table.y_top), table.xdims+2*rad, rad, fc='white', ec='none'))
    ax.add_patch(plt.Rectangle((table.x_left, table.y_bottom), 100, 200, fc='none'))
    
    plt.axis('scaled')
    plt.axis('off')
    
    return fig


def save_all_plot_frames(table, positions_plot, ball_color='blue', hole_color='darkred', directory='animation/frames', format='png'):
    """Iterates across all elements of positions_plot and plots each time. Saves each time as a frame in the directory chosen.
    table : object
        used to get the positions of the walls and holes and the radii of the balls and holes
    positions_plot : list
        list of arrays of positions of all of the balls at times separated by plot_interval
    ball_color : string
        color to make the balls in the plot
    hole_color : string
        color to make the holes in the plot
    directory : string
        the relative path to save the file to
    format : string
        file format to save the frames as
    """
    max_decimals = int(np.ceil(np.log10(len(positions_plot)+1)))    # used for filling in 0s at the start of the filename frame number
                                                                    # +1 to make 100, 1000, etc work correctly
                                                                    
    for i in range(len(positions_plot)):
        fig = plot_time_t_positions(table, positions_plot, i)
        frame_number = str(i+1).zfill(max_decimals)
        fig.savefig("{0}/frame {1}.{2}".format(directory, frame_number, format), format=format)
        plt.close()    # prevents overflow errors