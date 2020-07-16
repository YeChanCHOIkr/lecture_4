class Cat:
    color = 'red'

#생성자 매서드
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print('우리 {}이는 색깔이 {}이구요. 자주 야옹~! 야옹~! 거려요.'.format(self.name, self.color))

raon = Cat('라온', '똥')
raon.meow()

meon = Cat('미용', '컬러풀')
print(meon.color)
meon.meow()