import math
from base import Shape
class Elipse(Shape):
    def __init__(self,shortradius,longradius):
        super().__init__(name='Ellipse')# used to get information from parent
        self.shortradius=shortradius
        self.longradius=longradius
    
    def detect_shape(self):
        return f'the shape is {self.name} and radiuses are {self.shortradius} {self.longradius}'
    
    def contour_shape(self):
        return f'the shape contours around {self.name}'# coded contour and detect funcs
    
    def print_shape_info(self):
        print(f'Shapes name is {self.name}')
        print(f'Shapes area is {self.longradius*self.shortradius/2} ')