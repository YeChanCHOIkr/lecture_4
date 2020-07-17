class Cat:
    color = 'red'
    sound = '야용'

#생성자 매서드
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def meow(self, name, sound):
        print ('우리 고양이는 못생긴 {}이에요'.format(name))
        print('길냥이 {}이는 색깔이 {}이구요. 자주 {}~! {}~!거려요.'.format(self.name, self.color, self.sound, sound))

gang_cat = Cat('미옹', '컬러풀하','미아옹')
# jong_cat = Cat('태경', '똥')
gang_cat.meow('라온','미웅')
# jong_cat.meow('라온')