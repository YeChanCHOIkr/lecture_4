import math

class Circle : 
    def __init__(self, name, R, Pi) :
        self.name = name
        self.R = R
        self.Pi = Pi
    def area(self) :
        return self.Pi * (self.R**2)
    def __del__(self) :
        pass

c1 = Circle('A', 10, math.pi)
c2 = Circle('B', 9, math.pi)
c3 = Circle('C', 6, math.pi)
# c1.area()
# c2.area()
# c3.area()
print('{}의 면적은 {}'.format('A', c1.area()))
print('{}의 면적은 {}'.format('B', c2.area()))
print('{}의 면적은 {}'.format('C', c3.area()))

print(c1.__dict__)