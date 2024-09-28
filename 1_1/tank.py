class Tank:

    count =0

    def __init__(self,x,y,model,ammo):
        Tank.count += 1
        self.model = model
        self.hp = 100
        self.ammo = ammo
        self.xp = 0
        self.fuel = 100
        self.y = y
        self.x= x
        if self.x<0:
            self.x = 0
        if self.y<0:
            self.y = 0

    def fire(self):
        if self.ammo >0:
            self.ammo -= 1
            print('стреляю')

    def forvard(self):
        if self.fuel >0:
            self.y += -1
            self.fuel -= 1

    def dackward(self):
        if self.fuel >0:
            self.y += 1
            self.fuel -= 1

    def left(self):
        if self.fuel >0:
            self.x += -1
            self.fuel -= 1

    def right(self):
        if self.fuel >0:
            self.x += 1
            self.fuel -= 1

    def __str__(self):
        return(f'Танк: {self.model},'f'Здоровье: {self.hp},'
              f'Патроны:{self.ammo},опыт{self.xp},топливо{self.fuel},'
              f'Кординаты:({self.x},{self.y})')
