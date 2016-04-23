# This module creates the Objects for the balls, the balls on table, and the table itself
# PHY 494 - Billiard Simulation Final

#-------------------------------------------------------------------------------------------------------------------------------------------
# Define all of the Objects
#-------------------------------------------------------------------------------------------------------------------------------------------

# Define a Ball
class Ball(object):
    def __init__(self, name, mass, radius, position):
        
        self.name = name
        self.position = position
        
        if mass >= 0:
            self.mass = mass
        else:
            raise ValueError("Mass needs to be positive and nonzero")
        
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError("Radius needs to be positive and nonzero")
    
    def get_name(self):
        return self.name
    
    def get_mass(self):
        return self.mass
    
    def get_radius(self):
        return self.radius
    
    def get_position(self):
        return self.position

    
# Define the Holes
class Holes(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        return (self.x, self.y)
    
        
# Define the Table
class Table(object):
    
    def __init__(self):
        self.holes = []
        
    def add_holes(self, addition):
        self.holes.append(addition)
        
    def get_holes(self):
        return self.holes
    
    
# Define the Balls on Table
class Table_Balls(object):
    
    def __init__(self):
        self.balls = []
        
    def add_balls(self, addition):
        self.balls.append(addition)
        
    def get_balls(self):
        return self.balls
    
    def check_position(self, holes = Table.get_holes):
        for i,m in enumerate(holes):
            for j,t in enumerate(self.position):
                if t == m:
                    print("\'{}\' fell in hole.".format(m.get_name()))
                    self.position.remove(t)


#-------------------------------------------------------------------------------------------------------------------------------------------
# Declare the Objects
#-------------------------------------------------------------------------------------------------------------------------------------------

Table_Balls.add_balls(Ball(cue, 0.165, 5.7, (50,50))
Table_Balls.add_balls(Ball(ball_1, 0.165, 5.7, (30,100))
Table_Balls.add_balls(Ball(ball_2, 0.165, 5.7, (40,150))
Table_Balls.add_balls(Ball(ball_3, 0.165, 5.7, (60,150))
Table_Balls.add_balls(Ball(ball_4, 0.165, 5.7, (70,100))
print(Table_Balls.get_balls())
                      
#not sure if there is an easy way to add many points without having to type each one
Table.add_holes(Holes(