class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return '{}'.format(self.x & self.y)
        # return '({}, {})'.format(self.x, self.y)
    def eq(self, other) :
        return Vector2D(self.x == other.x, self.y == other.y)
    def __eq__(self, other) :
        return Vector2D(self.x == other.x, self.y == other.y)

v1 = Vector2D(3, 3)
v2 = Vector2D(3, 3)

# eq
v3 = v1.eq(v2)
print(v3)

# __eq__
v4 = v1 == v2
print(v4)