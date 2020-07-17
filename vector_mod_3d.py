class Vector3D :
    def __init__(self, x, y, z) :
        self.x = x
        self.y = y
        self.z = z
    def __str__(self) :
        return '({}, {}, {})'.format(self.x, self.y, self.z)
    def mod(self, other) :
        return Vector3D(self.x % other.x, self.y % other.y, self.z % other.z)
    def __mod__(self, other) :
        return Vector3D(self.x % other.x, self.y % other.y, self.z % other.z)

v1 = Vector3D(4, 5, 6)
v2 = Vector3D(1, 2, 3)

# mod
v3 = v1.mod(v2)
print(v3)

# __mod__
v4 = v1 % v2
print(v4)