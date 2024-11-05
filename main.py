import math
from base import Shape
from circle import Circle
from triangle import Triangle
from square import Square
from ellipse import Elipse#imported from parent and child clasess

circle1=Circle(5)
triangle1=Triangle(3,4,5)
square1=Square(4)
ellipse1=Elipse(3,4)#given the paramters

print(circle1.detect_shape())
print(circle1.contour_shape())
circle1.print_shape_info()

print(triangle1.detect_shape())
print(triangle1.contour_shape())
triangle1.print_shape_info()

print(square1.detect_shape())
print(square1.contour_shape())
square1.print_shape_info()

print(ellipse1.detect_shape())
print(ellipse1.contour_shape())
ellipse1.print_shape_info()