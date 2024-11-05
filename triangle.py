import math
from base import Shape
class Triangle(Shape):
    def __init__(self,a=float,b=float,c=float):
        super().__init__(name="triangle")# used to get information from parent
        self.a=a
        self.b=b
        self.c=c
    
    def detect_shape(self):
        return f'the shape is {self.name} and sides are {self.a} {self.b} {self.c}'
    
    def contour_shape(self):
        return f'the shape contours around {self.name}'# coded contour and detect funcs
    
    def print_shape_info(self):
        s=(self.a+self.b+self.c)/2
        total=self.a+self.b+self.c
        area= math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        
        print(f'Area is {area}')
        print(f'the Circumference is {total}')

