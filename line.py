<<<<<<< HEAD
import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
        
    # distance - RAIZ((c2 - c1)² + (d2 - d1)²)
    # slope - d2 - d1 / c2 - c1

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1,coordinate2)
print(str(line.distance()))
=======
import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)
        
    # distance - RAIZ((c2 - c1)² + (d2 - d1)²)
    # slope - d2 - d1 / c2 - c1

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1,coordinate2)
print(str(line.distance()))
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
print(str(line.slope()))