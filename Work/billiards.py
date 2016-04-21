import numpy as np

#converting velocity to speed for collisions
def vel2speed(velocities):
    """ Function converts a velocity from the array in speed
    which will make collision algorithms easier to write"""
    
    for i in range velocities:
        speeds  ((v[0])**2 + (v[1])**2)**0.5
    
    return speeds


#momentum transfer if initial ball completely stops
def momentumtransfer(velocities):
    """ Function reveals how the quantity of momentum p = mv
    is tranferred during a collision. Because mass is identical
    for every ball it can be neglected"""
    
    speeds = vel2speed(velocities)
    
    s1 = speeds[0:]
    s2 = speeds[1:]
    
    s2 = s2 + s1
    s1 = s1 - s1
    
    return s1, s2


#momentum transfer if initial ball stills has some speed
def momentumtransfer(velocities):
    """ Function reveals how the quantity of momentum p = mv
    is tranferred during a collision. Because mass is identical
    for every ball it can be neglected"""
    
    speeds = vel2speed(velocities)
    
    s1 = speeds[0:]
    s2 = speeds[1:]
    
    s2 = s2 + (s1*0.9)
    s1 = s1*0.1
    
    return s1, s2


#how to remove balls from table
def ballremoval(positions):
    """ This is written assuming the table is a box of 110 x 200
    but stills need a function called remove to do the job"""
    
    for i in range positions:
        if i is [0,0]:
            #remove
        if i is [0,100]:
            #remove
        if i is [0,200]:
            #remove
        if i is [100,0]:
            #remove
        if i is [100,100]:
            #remove
        if i is [100,200]:
            #remove
            
    return positions