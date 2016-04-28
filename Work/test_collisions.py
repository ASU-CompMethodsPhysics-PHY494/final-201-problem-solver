import numpy as np
import billiard_objects
import collisions
from numpy.testing import (assert_almost_equal)

#------------------------------------------------------------------------------
ball_1 = billiard_objects.Ball("test ball 1", 0.165, 5.7)
ball_2 = billiard_objects.Ball("test ball 2", 0.165, 5.7)    #balls have the same mass and radius 5.7
table = billiard_objects.Table(100, 200, 11.4)
table.add_balls(ball_1, ball_2)
#------------------------------------------------------------------------------


def reset_position_velocity(*balls):
    """Resets the positions and velocities to [0, 0]"""
    for ball in balls[0]:
        ball.set_position(np.zeros(2, dtype='float64'))
        ball.set_velocity(np.zeros(2, dtype='float64'))
        ball.reset_delta_velocity()
    
    
def test_1d_ball_collision():
    """Both balls positions and movement are only along the x-axis"""
    reset_position_velocity(table.balls)
    
    table.balls[0].set_velocity(np.array([2, 0]))    # ball_1 moving right at 2
    table.balls[1].set_position(np.array([5, 0]))    # ball_2 stationary at (5, 0) (within the radius of the other)
    collisions.ball_collisions(table.balls)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], -2)    # ball_1 should lose its velocity
    assert_almost_equal(table.balls[0].delta_velocity[1], 0)
    assert_almost_equal(table.balls[1].delta_velocity[0], 2)
    assert_almost_equal(table.balls[1].delta_velocity[1], 0)     # ball_2 should gain the velocity from ball_1
    
    
def test_2d_ball_collision():
    """One ball impacts at an angle"""
    reset_position_velocity(table.balls)
    
    table.balls[0].set_position(np.array([0, 2]))
    table.balls[0].set_velocity(np.array([2, 0]))    # ball_1 at (0, 2) and moving right at 2
    table.balls[1].set_position(np.array([2, 0]))    # ball_2 stationary at (2, 0)
    collisions.ball_collisions(table.balls)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], -1)    # ball_1 should lose half its velocity in the x-direction
    assert_almost_equal(table.balls[0].delta_velocity[1], 1)     # ball_1 should gain some upward velocity
    assert_almost_equal(table.balls[1].delta_velocity[0], 1)     
    assert_almost_equal(table.balls[1].delta_velocity[1], -1)    # ball_2 takes the rest of the velocities such that it conserves momentum
    
    
def test_left_wall_collision():
    reset_position_velocity(table.balls)
    
    table.balls[0].set_position(np.array([-45, 0]))    # ball_1 is at (-45, 0) which is close to hit the left wall (x=-50)
    table.balls[0].set_velocity(np.array([-2, 2]))     # ball_1 is moving up and left
    collisions.wall_collisions(table)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], 4)    # ball_1 should lose gain -2 times its velocity in x-direction
    assert_almost_equal(table.balls[0].delta_velocity[1], 0)     # y-direction velocity should be unchanged
    
    
def test_right_wall_collision():
    reset_position_velocity(table.balls)
    
    table.balls[0].set_position(np.array([45, 0]))    # ball_1 is at (45, 0) which is far enough to hit the right wall (x=50)
    table.balls[0].set_velocity(np.array([2, 2]))     # ball_1 is moving up and right
    collisions.wall_collisions(table)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], -4)    # ball_1 should lose gain -2 times its velocity in x-direction
    assert_almost_equal(table.balls[0].delta_velocity[1], 0)     # y-direction velocity should be unchanged
    
    
def test_bottom_wall_collision():
    reset_position_velocity(table.balls)
    
    table.balls[0].set_position(np.array([0, -95]))    # ball_1 is at (0, -95) which is close to hit the left wall (y=-100)
    table.balls[0].set_velocity(np.array([2, -2]))     # ball_1 is down and right
    collisions.wall_collisions(table)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], 0)    # x-direction velocity should be unchanged
    assert_almost_equal(table.balls[0].delta_velocity[1], 4)    # ball_1 should lose gain -2 times its velocity in y-direction
    
    
def test_top_wall_collision():
    reset_position_velocity(table.balls)
    
    table.balls[0].set_position(np.array([0, 95]))    # ball_1 is at (0, 95) which is close to hit the top wall (y=100)
    table.balls[0].set_velocity(np.array([2, 2]))     # ball_1 is up and right
    collisions.wall_collisions(table)
    
    assert_almost_equal(table.balls[0].delta_velocity[0], 0)    # x-direction velocity should be unchanged
    assert_almost_equal(table.balls[0].delta_velocity[1], -4)    # ball_1 should lose gain -2 times its velocity in y-direction