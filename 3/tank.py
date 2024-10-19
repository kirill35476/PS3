from hitbox import Hitbox

class Tank:

    __count = 0
    __SIZE = 100

    def __init__(self,x,y,canvas,model = 'Т-14 Армата',ammo = 100,
                 speed = 10):
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)
        Tank.__count += 1
        self.__canvas = canvas
        self.__model = model
        self.__hp = 100
        self.__ammo = ammo
        self.__xp = 0
        self.__fuel = 100
        self.__y = y
        self.__x = x
        self.__speed = speed
        if self.__x<0:
            self.__x = 0
        if self.__y<0:
            self.__y = 0

        self.__create()

    def fire(self):
        if self.__ammo >0:
            self.__ammo -= 1
            print('стреляю')

    def forvard(self):
        if self.__fuel >0:
            self.__y += - self.__speed
            self.__update_hitbox()
            self.__fuel -= 1
            self.__repaint()

    def dackward(self):
        if self.__fuel >0:
            self.__y += self.__speed
            self.__update_hitbox()
            self.__fuel -= 1
            self.__repaint()

    def left(self):
        if self.__fuel >0:
            self.__x += -self.__speed
            self.__update_hitbox()
            self.__fuel -= 1
            self.__repaint()

    def right(self):
        if self.__fuel >0:
            self.__x += self.__speed
            self.__update_hitbox()
            self.__fuel -= 1
            self.__repaint()

    def __create(self):
        self.id = self.__canvas.create_rectangle(self.__x, self.__y,
                                                 self.__x + Tank.__SIZE,
                                                 self.__y + Tank.__SIZE,
                                                 fill = 'red')

    def __repaint(self):
        self.__canvas.moveto(self.id, x= self.__x, y = self.__y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_model(self):
        return self.__model

    def get_hp(self):
        return self.__hp

    def get_xp(self):
        return  self.__xp

    def get_fuel(self):
        return  self.__fuel

    def get_speed(self):
        return  self.__speed

    @staticmethod
    def get_quantity():
        return Tank.__count

    @staticmethod
    def get_sise():
        return Tank.__SIZE

    def __str__(self):
        return(f'Танк: {self.__model},'f'Здоровье: {self.__hp},'
              f'Патроны:{self.__ammo},опыт{self.__xp},топливо{self.__fuel},'
              f'Кординаты:({self.__x},{self.__y})')