class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return '({}, {})'.format(self.x, self.y)
    def mod(self, other) :
        return Vector2D(self.x % other.x, self.y % other.y)
    def __mod__(self, other) :
        return Vector2D(self.x % other.x, self.y % other.y)

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

# mod
v3 = v1.mod(v2)
print(v3)

# __mod__
v4 = v1 % v2
print(v4)