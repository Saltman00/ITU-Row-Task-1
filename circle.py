import math
from base import Shape
class Circle(Shape):
    def __init__(self,radius):
        super().__init__(name='circle')#used super to get information from parent
        self.radius=radius
    
    def detect_shape(self):
            return f"detected {self.name} and radius is {self.radius}"
    
    def contour_shape(self):
            return f"counturing around the {self.name}"# coded contour and detect funcs
    
    def print_shape_info(self):
        print(f"Area: {math.pi * self.radius ** 2}")
        print(f"Circumference: {2 * math.pi * self.radius}")#calculated area and circumference
