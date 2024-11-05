import math
from base import Shape
class Square(Shape):
    def __init__(self,side=float):# used to get information from parent
        super().__init__(name='Square')
        self.side=side
    
    def detect_shape(self):
        return f'the shape is {self.name} and side is {self.side} '
    
    def contour_shape(self):
        return f'the shape contours around {self.name}'# coded contour and detect funcs
    
    def print_shape_info(self):
        area=self.side*self.side
        total=self.side*4
        
        print(f'Shapes area is {area} ')
        print(f'shapes circumrference is {total}')