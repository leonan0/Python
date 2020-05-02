class Cylinder():

    pi = 3.14

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        a = Cylinder.pi * (self.radius * self.radius) * self.height
        return a
        #return self.height*3.14*(self.radius)**2


    def surface_area(self):
        a = (2 * (Cylinder.pi * (self.radius * self.radius))) + (2 * Cylinder.pi * self.radius * self.height )         
        return a
        #top = 3.14 * (self.radius)**2
        #return (2*top) + (2*3.14*self.radius*self.height)

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())