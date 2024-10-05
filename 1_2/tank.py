class Tank:

    count = 0
    SIZE = 100

    def __init__(self,x,y,canvas,model = 'Т-14 Армата',ammo = 100,
                 speed = 10):
        Tank.count += 1
        self.canvas = canvas
        self.model = model
        self.hp = 100
        self.ammo = ammo
        self.xp = 0
        self.fuel = 100
        self.y = y
        self.x= x
        self.speed = speed
        if self.x<0:
            self.x = 0
        if self.y<0:
            self.y = 0

        self.create()

    def fire(self):
        if self.ammo >0:
            self.ammo -= 1
            print('стреляю')

    def forvard(self):
        if self.fuel >0:
            self.y += - self.speed
            self.fuel -= 1
            self.repaint()

    def dackward(self):
        if self.fuel >0:
            self.y += self.speed
            self.fuel -= 1
            self.repaint()

    def left(self):
        if self.fuel >0:
            self.x += -self.speed
            self.fuel -= 1
            self.repaint()

    def right(self):
        if self.fuel >0:
            self.x += self.speed
            self.fuel -= 1
            self.repaint()

    def create(self):
        self.id = self.canvas.create_rectangle(self.x,self.y,
                                               self.x + Tank.SIZE,
                                               self.y + Tank.SIZE,
                                               fill = 'red')

    def repaint(self):
        self.canvas.moveto(self.id,x= self.x,y = self.y)

    def __str__(self):
        return(f'Танк: {self.model},'f'Здоровье: {self.hp},'
              f'Патроны:{self.ammo},опыт{self.xp},топливо{self.fuel},'
              f'Кординаты:({self.x},{self.y})')