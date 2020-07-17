class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def eq(self, other) :
        data = self.x == other.x and self.y == other.y
        if(data) :
            return '같습니다.'
        else :
            return '다릅니다.'
    def __eq__(self, other) :
        data = self.x == other.x and self.y == other.y
        if(data) :
            return '같습니다.'
        else :
            return '다릅니다.'

v1 = Vector2D(3, 3)
v2 = Vector2D(4, 3)

# eq
v3 = v1.eq(v2)
print(v3)

# __eq__
v4 = v1 == v2
print(v4)