class Vector2D :
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = (self.x**2 + self.y**2)**0.5
    def __str__(self) :
        return '{}'.format(self.z)
    def eq(self, other) :
        return Vector2D((self.x**2 + self.y**2)**0.5 == (other.x**2 + other.y**2)**0.5,)
    def __eq__(self, other) :
        return Vector2D((self.x**2 + self.y**2)**0.5 == (other.x**2 + other.y**2)**0.5,)

v1 = Vector2D(3, 2)
v2 = Vector2D(3, 4)

# eq
v3 = v1.eq(v2)
print(v3)

# __eq__
v4 = v1 == v2
print(v4)