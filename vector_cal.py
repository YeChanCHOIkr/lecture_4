class Vector2D :
    # init : 메모리 사용 시작
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return '({}, {})'.format(self.x, self.y)


    def eq(self, other) :
        return Vector2D(self.x == other.x, self.y == other.y)
    def __eq__(self, other) :
        return Vector2D(self.x == other.x, self.y == other.y)

    def add(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)
    def __add__(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other) :
        return Vector2D(self.x - other.x, self.y - other.y)
    def __sub__(self, other) :
        return Vector2D(self.x - other.x, self.y - other.y)

    def mod(self, other) :
        return Vector2D(self.x % other.x, self.y % other.y)
    def __mod__(self, other) :
        return Vector2D(self.x % other.x, self.y % other.y)

    # 메모리 사용 종료
    def __del__(self) :
        print('종료')