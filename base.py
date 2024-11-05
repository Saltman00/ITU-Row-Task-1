import math
class Shape:#created a shape parent class
    def __init__(self,name='not yet detected'):
        self.name=name
    
    def detect_shape(self):
        pass#coded in sublcasses
    
    def contour_shape(self):
        pass#coded in subclasess
   
    def print_shape_info(self):
        pass#coded in subclasess
