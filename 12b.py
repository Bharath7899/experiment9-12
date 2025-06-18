class shape:
 def  _init_(self,color):
    self.color=color
def area(self):
    pass
class circle(shape):
 def _init_(self,color,radius):
        super()._init_(color)
        self.radius=radius
def area(self):
    return 3.14*self.radius**2
class rectangle(shape):
 def _init_(self,color,width,height):
     super()._init_(color)
self.width=width
self.height=height
def area(self):
 return self.width*self.height
circle=circle("red",5)
rectangle=rectangle("blue",4,6)
print("circle area:",circle.area())
print("rectangle area:",rectangle.area())
